<?php
/**
 * Plugin Name: Getting What You Want Calculator
 * Plugin URI: https://github.com/Quickinfinity/GWYW-TOOL
 * Description: GWYW Business Calculator with admin settings. Use shortcode [gwyw_calculator]
 * Version: 2.0.0
 * Author: Joe Quick
 * Author URI: https://joequick.com
 * License: GPL v2 or later
 */

if (!defined('ABSPATH')) exit;

// ============================================================
// ADMIN SETTINGS PAGE
// ============================================================

function gwyw_get_defaults() {
    return array(
        'product_system'  => 'graniflex',
        'price_per_sqft'  => '8.00',
        'gp_target'       => '100000',
        'working_weeks'   => '42',
        'num_techs'       => '3',
        'tech1_rate'      => '30',
        'tech2_rate'      => '25',
        'tech3_rate'      => '18',
        'lead_to_quote'   => '30',
        'quote_to_close'  => '60',
        'operating_pct'   => '8',
        'marketing_pct'   => '10',
        'business_exp_pct'=> '10',
        'sales_comm_pct'  => '5',
        'drive_time'      => '2',
    );
}

function gwyw_get_settings() {
    return wp_parse_args(get_option('gwyw_settings', array()), gwyw_get_defaults());
}

function gwyw_admin_menu() {
    add_menu_page(
        'GWYW Calculator Settings',
        'GWYW Calculator',
        'manage_options',
        'gwyw-settings',
        'gwyw_settings_page',
        'dashicons-calculator',
        80
    );
}
add_action('admin_menu', 'gwyw_admin_menu');

function gwyw_settings_init() {
    register_setting('gwyw_settings_group', 'gwyw_settings', 'gwyw_sanitize_settings');

    add_settings_section('gwyw_main', 'Default Calculator Values', function() {
        echo '<p>These values pre-populate the calculator when visitors load the page. Users can still change them.</p>';
    }, 'gwyw-settings');

    $fields = array(
        'product_system'  => array('Default Product System', 'select', array('graniflex'=>'Graniflex Floor System','rcw_ext'=>'Rustic Concrete Wood (Ext)')),
        'price_per_sqft'  => array('Charge $/sqft', 'number', array('step'=>'0.25','min'=>'0')),
        'gp_target'       => array('Gross Profit Target ($)', 'number', array('step'=>'5000','min'=>'0')),
        'working_weeks'   => array('Working Weeks / Year', 'number', array('step'=>'1','min'=>'1','max'=>'52')),
        'num_techs'       => array('Number of Techs', 'number', array('step'=>'1','min'=>'1','max'=>'20')),
        'tech1_rate'      => array('Tech 1 $/hr', 'number', array('step'=>'1','min'=>'0')),
        'tech2_rate'      => array('Tech 2 $/hr', 'number', array('step'=>'1','min'=>'0')),
        'tech3_rate'      => array('Tech 3 $/hr', 'number', array('step'=>'1','min'=>'0')),
        'lead_to_quote'   => array('Lead → Quote %', 'number', array('step'=>'1','min'=>'0','max'=>'100')),
        'quote_to_close'  => array('Quote → Close %', 'number', array('step'=>'1','min'=>'0','max'=>'100')),
        'operating_pct'   => array('Operating Cost %', 'number', array('step'=>'1','min'=>'0')),
        'marketing_pct'   => array('Marketing + Ad %', 'number', array('step'=>'1','min'=>'0')),
        'business_exp_pct'=> array('Business Expense %', 'number', array('step'=>'1','min'=>'0')),
        'sales_comm_pct'  => array('Sales Commission %', 'number', array('step'=>'1','min'=>'0')),
        'drive_time'      => array('Drive Time (hrs/tech)', 'number', array('step'=>'0.5','min'=>'0')),
    );

    foreach ($fields as $key => $info) {
        add_settings_field('gwyw_' . $key, $info[0], 'gwyw_render_field', 'gwyw-settings', 'gwyw_main', array('key'=>$key,'type'=>$info[1],'opts'=>$info[2]));
    }
}
add_action('admin_init', 'gwyw_settings_init');

function gwyw_render_field($args) {
    $s = gwyw_get_settings();
    $val = esc_attr($s[$args['key']]);
    $name = 'gwyw_settings[' . $args['key'] . ']';
    if ($args['type'] === 'select') {
        echo '<select name="' . $name . '">';
        foreach ($args['opts'] as $k => $label) {
            echo '<option value="' . esc_attr($k) . '"' . selected($val, $k, false) . '>' . esc_html($label) . '</option>';
        }
        echo '</select>';
    } else {
        $attrs = '';
        foreach ($args['opts'] as $k => $v) $attrs .= ' ' . $k . '="' . esc_attr($v) . '"';
        echo '<input type="number" name="' . $name . '" value="' . $val . '"' . $attrs . ' class="regular-text" />';
    }
}

function gwyw_sanitize_settings($input) {
    $defaults = gwyw_get_defaults();
    $out = array();
    foreach ($defaults as $key => $def) {
        $out[$key] = isset($input[$key]) ? sanitize_text_field($input[$key]) : $def;
    }
    return $out;
}

function gwyw_settings_page() {
    if (!current_user_can('manage_options')) return;
    ?>
    <div class="wrap">
        <h1>GWYW Calculator Settings</h1>
        <form method="post" action="options.php">
            <?php
            settings_fields('gwyw_settings_group');
            do_settings_sections('gwyw-settings');
            submit_button('Save Defaults');
            ?>
        </form>
        <hr>
        <p><strong>Shortcode:</strong> <code>[gwyw_calculator]</code></p>
        <p>Place this shortcode on any page to display the calculator.</p>
    </div>
    <?php
}

function gwyw_calculator_settings_link($links) {
    $settings_link = '<a href="' . admin_url('admin.php?page=gwyw-settings') . '">Settings</a>';
    array_unshift($links, $settings_link);
    return $links;
}
add_filter('plugin_action_links_' . plugin_basename(__FILE__), 'gwyw_calculator_settings_link');

// ============================================================
// ENQUEUE ASSETS
// ============================================================

function gwyw_enqueue_assets() {
    global $post;
    if (!is_a($post, 'WP_Post') || !has_shortcode($post->post_content, 'gwyw_calculator')) return;
    wp_enqueue_style('gwyw-fonts', 'https://fonts.googleapis.com/css2?family=Bebas+Neue&family=JetBrains+Mono:wght@400;600;700&family=Outfit:wght@300;400;500;600;700;800&display=swap', array(), null);
    wp_enqueue_script('gwyw-jspdf', 'https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js', array(), '2.5.1', true);
}
add_action('wp_enqueue_scripts', 'gwyw_enqueue_assets');

// ============================================================
// SHORTCODE: EMBEDDED CALCULATOR
// ============================================================

function gwyw_calculator_shortcode($atts) {
    $s = gwyw_get_settings();
    $crew_rates = array(floatval($s['tech1_rate']), floatval($s['tech2_rate']), floatval($s['tech3_rate']));
    $num_techs = intval($s['num_techs']);
    $crew_json = wp_json_encode(array_slice($crew_rates, 0, $num_techs));

    ob_start();
    ?>
<style>
#gwyw-calc{--bg:#0f1117;--c1:#181b24;--c2:#1e222e;--inp:#252a38;--bd:#2a2f3e;--bd2:#3d4458;--y:#f5c518;--yd:#c49e0f;--yg:rgba(245,197,24,.15);--g:#34d399;--r:#f87171;--b:#60a5fa;--o:#fb923c;--p:#a78bfa;--t:#2dd4bf;--t1:#e8eaf0;--t2:#8b92a5;--t3:#5a6178;--tl:#9ca3b8;font-family:'Outfit',sans-serif;background:var(--bg);color:var(--t1);line-height:1.5;box-sizing:border-box}
#gwyw-calc *{box-sizing:border-box;margin:0;padding:0}
#gwyw-calc ::-webkit-scrollbar{width:6px}#gwyw-calc ::-webkit-scrollbar-track{background:var(--bg)}#gwyw-calc ::-webkit-scrollbar-thumb{background:var(--bd2);border-radius:3px}
#gwyw-calc .hdr{background:linear-gradient(135deg,#0f1117,#1a1d2b,#0f1117);border-bottom:2px solid var(--y);padding:24px 32px;position:sticky;top:0;z-index:100;box-shadow:0 4px 30px rgba(0,0,0,.5)}
#gwyw-calc .hi{max-width:1400px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px}
#gwyw-calc .hdr h1{font-family:'Bebas Neue',sans-serif;font-size:2.2rem;letter-spacing:3px;color:var(--y);line-height:1}
#gwyw-calc .hdr .sub{font-size:.82rem;color:var(--t2);letter-spacing:1px;font-weight:300}
#gwyw-calc .hdr .br{text-align:right;font-size:.72rem;color:var(--t3)}#gwyw-calc .hdr .br strong{color:var(--t2)}
#gwyw-calc .nav{background:var(--c1);border-bottom:1px solid var(--bd);position:sticky;top:82px;z-index:99;overflow-x:auto}
#gwyw-calc .ni{max-width:1400px;margin:0 auto;display:flex}
#gwyw-calc .nb{font-family:'Outfit',sans-serif;font-size:.72rem;font-weight:600;letter-spacing:.6px;text-transform:uppercase;padding:12px 18px;border:none;background:0 0;color:var(--t2);cursor:pointer;white-space:nowrap;border-bottom:2px solid transparent;transition:.2s}
#gwyw-calc .nb:hover{color:var(--t1);background:rgba(245,197,24,.04)}#gwyw-calc .nb.ac{color:var(--y);border-bottom-color:var(--y);background:rgba(245,197,24,.06)}
#gwyw-calc .nb .step{display:inline-block;width:18px;height:18px;line-height:18px;text-align:center;border-radius:50%;background:var(--bd);color:var(--t3);font-size:.6rem;font-weight:700;margin-right:6px}
#gwyw-calc .nb.ac .step{background:var(--y);color:#000}
#gwyw-calc .mc{max-width:1400px;margin:0 auto;padding:28px 24px 80px}
#gwyw-calc .sec{display:none;animation:gwyw-fi .3s ease}#gwyw-calc .sec.ac{display:block}
@keyframes gwyw-fi{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}
#gwyw-calc .sh{margin-bottom:24px;padding-bottom:14px;border-bottom:1px solid var(--bd)}#gwyw-calc .sh h2{font-family:'Bebas Neue',sans-serif;font-size:1.7rem;letter-spacing:2px;margin-bottom:2px}
#gwyw-calc .sh p{font-size:.85rem;color:var(--t2);max-width:700px}
#gwyw-calc .sh .step-label{font-size:.7rem;text-transform:uppercase;letter-spacing:1.5px;color:var(--t);font-weight:600;margin-bottom:4px}
#gwyw-calc .cd{background:var(--c1);border:1px solid var(--bd);border-radius:10px;padding:22px;margin-bottom:18px}
#gwyw-calc .ct{font-family:'Bebas Neue',sans-serif;font-size:1.05rem;letter-spacing:1.5px;color:var(--y);margin-bottom:14px;display:flex;align-items:center;gap:8px}
#gwyw-calc .ct .ic{width:26px;height:26px;border-radius:6px;display:flex;align-items:center;justify-content:center;font-size:13px;flex-shrink:0}
#gwyw-calc .iy{background:rgba(245,197,24,.15);color:var(--y)}#gwyw-calc .ig{background:rgba(52,211,153,.15);color:var(--g)}#gwyw-calc .ib{background:rgba(96,165,250,.15);color:var(--b)}#gwyw-calc .ir{background:rgba(248,113,113,.15);color:var(--r)}#gwyw-calc .io{background:rgba(251,146,60,.15);color:var(--o)}#gwyw-calc .ip{background:rgba(167,139,250,.15);color:var(--p)}#gwyw-calc .it{background:rgba(45,212,191,.15);color:var(--t)}
#gwyw-calc .g2{display:grid;grid-template-columns:1fr 1fr;gap:18px}
#gwyw-calc .g3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:18px}
#gwyw-calc .g4{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
@media(max-width:900px){#gwyw-calc .g2,#gwyw-calc .g3,#gwyw-calc .g4{grid-template-columns:1fr}}
@media(min-width:901px) and (max-width:1100px){#gwyw-calc .g3,#gwyw-calc .g4{grid-template-columns:1fr 1fr}}
#gwyw-calc .ig2{margin-bottom:12px}#gwyw-calc .ig2 label{display:block;font-size:.68rem;font-weight:600;letter-spacing:.8px;text-transform:uppercase;color:var(--tl);margin-bottom:4px}
#gwyw-calc .ig2 input,#gwyw-calc .ig2 select{width:100%;background:var(--inp);border:1px solid var(--bd);border-radius:6px;color:var(--t1);font-family:'JetBrains Mono',monospace;font-size:.9rem;font-weight:600;padding:9px 12px;transition:.2s}
#gwyw-calc .ig2 input:focus,#gwyw-calc .ig2 select:focus{outline:none;border-color:var(--y);box-shadow:0 0 0 3px var(--yg)}
#gwyw-calc .ig2 input.ed{background:rgba(245,197,24,.08);border-color:var(--yd)}#gwyw-calc .ig2 .hn{font-size:.65rem;color:var(--t3);margin-top:2px}
#gwyw-calc .rr{display:flex;justify-content:space-between;align-items:center;padding:9px 0;border-bottom:1px solid rgba(42,47,62,.5);font-size:.85rem}#gwyw-calc .rr:last-child{border-bottom:none}#gwyw-calc .rr .lb{color:var(--t2)}
#gwyw-calc .rr .vl{font-family:'JetBrains Mono',monospace;font-weight:700;font-size:.88rem}
#gwyw-calc .rr.tot{border-top:2px solid var(--bd2);border-bottom:2px solid var(--bd2);padding:12px 0;margin-top:4px}#gwyw-calc .rr.tot .lb{color:var(--t1);font-weight:700;text-transform:uppercase;letter-spacing:.5px;font-size:.78rem}#gwyw-calc .rr.tot .vl{font-size:1.1rem}
#gwyw-calc .sg{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:12px;margin-bottom:18px}
#gwyw-calc .sx{background:var(--c2);border:1px solid var(--bd);border-radius:8px;padding:16px;text-align:center}
#gwyw-calc .sx .sl2{font-size:.65rem;font-weight:600;letter-spacing:1px;text-transform:uppercase;color:var(--t3);margin-bottom:6px}
#gwyw-calc .sx .sv{font-family:'JetBrains Mono',monospace;font-size:1.5rem;font-weight:700}#gwyw-calc .sx .ss{font-size:.68rem;color:var(--t3);margin-top:3px}
#gwyw-calc .dt{width:100%;border-collapse:collapse;font-size:.82rem}
#gwyw-calc .dt th{text-align:left;font-size:.65rem;font-weight:700;letter-spacing:.8px;text-transform:uppercase;color:var(--t3);padding:8px 12px;border-bottom:1px solid var(--bd);background:var(--c2)}
#gwyw-calc .dt td{padding:8px 12px;border-bottom:1px solid rgba(42,47,62,.4);color:var(--t2)}#gwyw-calc .dt td:first-child{color:var(--t1);font-weight:500}
#gwyw-calc .dt .mn{font-family:'JetBrains Mono',monospace;font-weight:600}#gwyw-calc .dt tr:hover td{background:rgba(245,197,24,.03)}
#gwyw-calc .fn{display:flex;flex-direction:column;gap:4px;max-width:650px;margin:0 auto 20px}
#gwyw-calc .fs{display:flex;align-items:center;justify-content:space-between;padding:12px 20px;border-radius:8px;position:relative;overflow:hidden}
#gwyw-calc .fs .fb{position:absolute;left:0;top:0;bottom:0;opacity:.12;border-radius:8px;transition:width .5s}#gwyw-calc .fs .fl{position:relative;font-weight:600;font-size:.82rem;z-index:1}
#gwyw-calc .fs .fv{position:relative;font-family:'JetBrains Mono',monospace;font-weight:700;font-size:1rem;z-index:1}#gwyw-calc .fs .fa{position:absolute;left:50%;bottom:-12px;transform:translateX(-50%);color:var(--t3);font-size:.7rem;z-index:2}
#gwyw-calc .lsb{display:flex;height:28px;border-radius:6px;overflow:hidden;margin:14px 0}#gwyw-calc .lsb .seg{display:flex;align-items:center;justify-content:center;font-size:.6rem;font-weight:700;color:#fff}
#gwyw-calc .qb{background:rgba(245,197,24,.05);border-left:3px solid var(--y);padding:14px 18px;margin:16px 0;border-radius:0 6px 6px 0}
#gwyw-calc .qb .qt{font-style:italic;color:var(--t2);font-size:.85rem;line-height:1.6}#gwyw-calc .qb .qa{color:var(--yd);font-size:.72rem;margin-top:4px;font-weight:600}
#gwyw-calc .pr{color:var(--g)!important}#gwyw-calc .pc{color:var(--r)!important}#gwyw-calc .pp{color:var(--y)!important}
#gwyw-calc .pm{background:linear-gradient(135deg,rgba(45,212,191,.05),rgba(245,197,24,.05));border:1px solid var(--t);border-radius:10px;padding:18px 22px;margin-bottom:18px}
#gwyw-calc .pm .pt{font-family:'Bebas Neue',sans-serif;font-size:1rem;letter-spacing:1.5px;color:var(--t);margin-bottom:10px}
#gwyw-calc .pr2{display:grid;grid-template-columns:1fr 100px 120px;gap:6px;padding:7px 0;border-bottom:1px solid rgba(42,47,62,.4);align-items:center;font-size:.85rem}
#gwyw-calc .pr2:last-child{border-bottom:none}#gwyw-calc .pr2 .pl{color:var(--t2)}#gwyw-calc .pr2 .pp2{font-family:'JetBrains Mono',monospace;font-weight:600;text-align:right}
#gwyw-calc .pr2 .pt2{font-family:'JetBrains Mono',monospace;font-weight:700;text-align:right}
#gwyw-calc .pr2.ph .pl{color:var(--t3);font-size:.65rem;font-weight:700;letter-spacing:.8px;text-transform:uppercase}
#gwyw-calc .pr2.pgp{border-top:2px solid var(--bd2);padding-top:10px;margin-top:4px}#gwyw-calc .pr2.pgp .pl{color:var(--t1);font-weight:700}
#gwyw-calc .vis{background:linear-gradient(135deg,rgba(245,197,24,.1),rgba(52,211,153,.06));border:2px solid var(--y);border-radius:12px;padding:24px;margin-bottom:20px}
#gwyw-calc .vis h3{font-family:'Bebas Neue',sans-serif;font-size:1.3rem;letter-spacing:2px;color:var(--y);margin-bottom:14px}
#gwyw-calc .vis .vr{display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid rgba(42,47,62,.4);font-size:.88rem}
#gwyw-calc .vis .vr:last-child{border-bottom:none}#gwyw-calc .vis .vr .vl2{color:var(--t2)}#gwyw-calc .vis .vr .vv{font-family:'JetBrains Mono',monospace;font-weight:700}
#gwyw-calc .vis .hero-total{display:flex;justify-content:space-between;align-items:center;border-top:3px solid var(--y);padding-top:14px;margin-top:10px}
#gwyw-calc .vis .hero-total .vl2{color:var(--t1);font-weight:700;font-size:1rem;font-family:'Bebas Neue',sans-serif;letter-spacing:1.5px}
#gwyw-calc .vis .hero-total .vv{color:var(--y);font-size:1.5rem}
#gwyw-calc .eq-ctx{background:var(--c2);border:1px solid var(--bd);border-radius:8px;padding:12px 18px;display:flex;gap:24px;flex-wrap:wrap;margin-bottom:14px;font-size:.82rem}
#gwyw-calc .eq-ctx .ec-item{display:flex;align-items:center;gap:6px}#gwyw-calc .eq-ctx .ec-label{color:var(--t3);font-size:.68rem;text-transform:uppercase;letter-spacing:.5px;font-weight:600}
#gwyw-calc .eq-ctx .ec-val{font-family:'JetBrains Mono',monospace;font-weight:700;color:var(--t)}
#gwyw-calc .divider{border:none;border-top:1px solid var(--bd);margin:8px 0}
@media(max-width:700px){#gwyw-calc .hdr h1{font-size:1.6rem}#gwyw-calc .hdr{padding:16px}#gwyw-calc .nav{top:70px}#gwyw-calc .mc{padding:18px 12px 60px}#gwyw-calc .cd{padding:16px}#gwyw-calc .sx .sv{font-size:1.2rem}#gwyw-calc .nb{padding:10px 12px;font-size:.66rem}}
</style>

<div id="gwyw-calc">
<div class="hdr"><div class="hi"><div><h1>GETTING WHAT YOU WANT</h1><div class="sub">Business Growth Calculator &mdash; Rules &amp; Tools</div></div><div style="display:flex;align-items:center;gap:16px"><button onclick="gwyw_generatePDF()" style="padding:8px 18px;background:rgba(245,197,24,.1);border:1.5px solid var(--y);border-radius:6px;color:var(--y);font-family:'Outfit',sans-serif;font-weight:600;font-size:.75rem;cursor:pointer;letter-spacing:.8px;text-transform:uppercase;white-space:nowrap;transition:.2s" onmouseover="this.style.background='rgba(245,197,24,.25)'" onmouseout="this.style.background='rgba(245,197,24,.1)'">&#x1F4C4; Download Report</button><div class="br"><strong>The Concrete Protector</strong> &middot; I-BOS System</div></div></div></div>

<div class="nav"><div class="ni">
<button class="nb ac" onclick="gwyw_go('vis',event)"><span class="step">1</span>Vision &amp; Inputs</button>
<button class="nb" onclick="gwyw_go('plan',event)"><span class="step">2</span>The Plan</button>
<button class="nb" onclick="gwyw_go('proj',event)"><span class="step">3</span>Project Model</button>
<button class="nb" onclick="gwyw_go('labor',event)"><span class="step">4</span>Labor &amp; Equipment</button>
<button class="nb" onclick="gwyw_go('tgt',event)"><span class="step">5</span>Target Areas</button>
</div></div>

<div class="mc">

<div class="sec ac" id="s-vis">
<div class="sh"><div class="step-label">Step 1 &mdash; Set Everything</div><h2>Your Vision &amp; Business Inputs</h2></div>
<div class="qb"><div class="qt">"There's only a few levers in your business. And when you learn how to pull the levers right, we can then make a predictive model on the profit that we will make."</div><div class="qa">&mdash; Joe Quick</div></div>
<div class="g2">
<div class="cd"><div class="ct"><span class="ic it">&#x2699;</span> Product &amp; Project</div>
<div class="ig2"><label>Product System</label><select id="gwyw-ps" class="ed" onchange="gwyw_onSys()"><option value="graniflex">Graniflex Floor System &mdash; $2.65/sqft</option><option value="rcw_ext">Rustic Concrete Wood (Ext) &mdash; $1.15/sqft</option></select></div>
<div class="g2"><div class="ig2"><label>Target Area</label><select id="gwyw-tat" class="ed" onchange="gwyw_preset()"><option value="custom">Custom</option><option value="garage" selected>Garage (576)</option><option value="basement">Basement (1,200)</option><option value="pool">Pool Deck (1,500)</option><option value="driveway">Driveway (1,800)</option><option value="firestation">Fire Station (5,000)</option><option value="walmart">Walmart (200,000)</option><option value="factory">Factory (100,000)</option></select></div><div class="ig2"><label>Sq Ft</label><input type="number" id="gwyw-sqft" value="576" class="ed" oninput="gwyw_calc()"></div></div>
<div class="g2"><div class="ig2"><label>Charge $/sqft</label><input type="number" id="gwyw-psf" value="<?php echo esc_attr($s['price_per_sqft']); ?>" step=".25" class="ed" oninput="gwyw_calc()"></div><div class="ig2"><label>COGS $/sqft</label><input type="number" id="gwyw-cog" value="2.65" step=".05" class="ed" oninput="gwyw_calc()"></div></div>
<div class="ig2"><label>Repair Charges $</label><input type="number" id="gwyw-rep" value="0" class="ed" oninput="gwyw_calc()"></div>
</div>
<div class="cd"><div class="ct"><span class="ic iy">&#x1F3AF;</span> The Master Number</div>
<div class="ig2"><label>Gross Profit Target ($)</label><input type="number" id="gwyw-tgp" value="<?php echo esc_attr($s['gp_target']); ?>" step="5000" class="ed" oninput="gwyw_calc()"><div class="hn">This is what pays for everything in your business</div></div>
<div class="ig2"><label>Working Weeks / Year</label><input type="number" id="gwyw-wwy" value="<?php echo esc_attr($s['working_weeks']); ?>" class="ed" oninput="gwyw_calc()"></div>
<div style="background:rgba(245,197,24,.1);border:1px solid var(--y);border-radius:8px;padding:12px;text-align:center;margin-top:8px"><div style="font-size:.65rem;font-weight:600;letter-spacing:1px;text-transform:uppercase;color:var(--t3);margin-bottom:4px">Projects Needed</div><div id="gwyw-projNeeded" style="font-family:'JetBrains Mono',monospace;font-size:1.6rem;font-weight:700;color:var(--y)">44</div><div id="gwyw-projPerWk" style="font-size:.7rem;color:var(--t3);margin-top:2px"></div></div>
<hr class="divider">
<div class="g2"><div class="ig2"><label>Lead &rarr; Quote %</label><input type="number" id="gwyw-lcr" value="<?php echo esc_attr($s['lead_to_quote']); ?>" class="ed" oninput="gwyw_calc()"></div><div class="ig2"><label>Quote &rarr; Close %</label><input type="number" id="gwyw-ccr" value="<?php echo esc_attr($s['quote_to_close']); ?>" class="ed" oninput="gwyw_calc()"></div></div>
</div>
</div>

<div class="g2">
<div class="cd"><div class="ct"><span class="ic io">&#x2699;</span> Equipment</div>
<div class="ig2"><label>Warrior Equipment</label><select id="gwyw-eqs" class="ed" onchange="gwyw_calc()"><option value="0" data-sqfthr="500" data-name="2047.4H">2047.4H &mdash; 500 sq ft/hr</option><option value="1" data-sqfthr="800" data-name="Samson 2756">Samson 2756 &mdash; 800 sq ft/hr</option><option value="2" data-sqfthr="1200" data-name="Leonidas 2795">Leonidas 2795 &mdash; 1,200 sq ft/hr</option><option value="3" data-sqfthr="2000" data-name="Leonidas 2795P">Leonidas 2795P &mdash; 2,000 sq ft/hr</option></select></div>
<div class="ig2"><label>Has Removal?</label><select id="gwyw-rmv" class="ed" onchange="gwyw_calc()"><option value="no">No Removal</option><option value="yes">Yes &mdash; Double Time</option></select></div>
</div>
<div class="cd"><div class="ct"><span class="ic iy">&#x26A1;</span> Crew <span id="gwyw-crewCount" style="color:var(--t);margin-left:auto;font-size:.75rem"></span></div>
<div id="gwyw-crewInputs"></div>
<div style="display:flex;gap:8px;margin-top:8px"><button onclick="gwyw_addTech()" style="flex:1;padding:8px;background:rgba(52,211,153,.15);border:1px solid var(--g);border-radius:6px;color:var(--g);font-family:'Outfit',sans-serif;font-weight:600;font-size:.75rem;cursor:pointer;letter-spacing:.5px">+ ADD TECH</button><button onclick="gwyw_removeTech()" id="gwyw-rmBtn" style="flex:1;padding:8px;background:rgba(248,113,113,.1);border:1px solid var(--r);border-radius:6px;color:var(--r);font-family:'Outfit',sans-serif;font-weight:600;font-size:.75rem;cursor:pointer;letter-spacing:.5px">&minus; REMOVE</button></div>
</div>
</div>

<div class="g2">
<div class="cd"><div class="ct"><span class="ic ir">&#x2699;</span> Below-the-Line Levers</div>
<div class="g2"><div class="ig2"><label>Operating Cost %</label><input type="number" id="gwyw-opc" value="<?php echo esc_attr($s['operating_pct']); ?>" step="1" class="ed" oninput="gwyw_calc()"></div><div class="ig2"><label>Marketing + Ad %</label><input type="number" id="gwyw-mkp" value="<?php echo esc_attr($s['marketing_pct']); ?>" step="1" class="ed" oninput="gwyw_calc()"></div></div>
<div class="g2"><div class="ig2"><label>Business Exp %</label><input type="number" id="gwyw-bep" value="<?php echo esc_attr($s['business_exp_pct']); ?>" step="1" class="ed" oninput="gwyw_calc()"></div><div class="ig2"><label>Drive Time (hrs/tech)</label><input type="number" id="gwyw-dth" value="<?php echo esc_attr($s['drive_time']); ?>" step=".5" class="ed" oninput="gwyw_calc()"><div class="hn">Round trip per job per tech</div></div></div>
<div class="ig2"><label>Sales Comm %</label><input type="number" id="gwyw-scp2" value="<?php echo esc_attr($s['sales_comm_pct']); ?>" step="1" class="ed" oninput="gwyw_calc()"></div>
</div>
<div class="cd"><div class="ct"><span class="ic ip">&#x1F4E1;</span> Lead Source Mix (%)</div>
<div class="g2"><div class="ig2"><label>Inbound Calls %</label><input type="number" id="gwyw-sp1" value="25" step="1" class="ed" oninput="gwyw_calc()"></div><div class="ig2"><label>Website Forms %</label><input type="number" id="gwyw-sp2" value="15" step="1" class="ed" oninput="gwyw_calc()"></div></div>
<div class="g2"><div class="ig2"><label>Mailers %</label><input type="number" id="gwyw-sp3" value="25" step="1" class="ed" oninput="gwyw_calc()"></div><div class="ig2"><label>Referrals %</label><input type="number" id="gwyw-sp4" value="25" step="1" class="ed" oninput="gwyw_calc()"></div></div>
<div class="g2"><div class="ig2"><label>Repeat %</label><input type="number" id="gwyw-sp5" value="10" step="1" class="ed" oninput="gwyw_calc()"></div><div class="ig2"><label>Mix Total</label><input type="text" id="gwyw-spTot" readonly style="font-weight:700"></div></div>
</div>
</div>

</div>

<div class="sec" id="s-plan">
<div class="sh"><div class="step-label">Step 2 &mdash; The Story</div><h2>Getting What You Want</h2></div>
<div id="gwyw-revChain" style="display:flex;align-items:center;justify-content:center;gap:0;flex-wrap:wrap;margin-bottom:20px;padding:16px;background:var(--c1);border:1px solid var(--bd);border-radius:10px"></div>
<div class="qb"><div class="qt">"Keep Score Weekly to Stay on Target. What gets measured gets done!"</div><div class="qa">&mdash; Joe Quick, learned from EOS</div></div>
<div class="vis" id="gwyw-ownerV"></div>
<div class="cd"><div class="ct"><span class="ic ig">&#x1F4CA;</span> P&amp;L Scorecard &mdash; Lagging Indicators</div>
<p style="font-size:.72rem;color:var(--t3);margin-bottom:14px">"Top line is vanity. Bottom line is sanity. Cash flow is reality."</p>
<div class="sg" id="gwyw-pnlS"></div>
<div id="gwyw-pnlR"></div></div>
<div class="cd"><div class="ct"><span class="ic iy">&#x1F4C8;</span> Profit Rules</div>
<div class="g4">
<div class="sx" style="border-color:var(--r)"><div class="sl2">Stop Growing</div><div class="sv" style="color:var(--r)">10%</div><div class="ss">10% = zero. Stabilize.</div></div>
<div class="sx" style="border-color:var(--y)"><div class="sl2">Time to Grow</div><div class="sv" style="color:var(--y)">15%</div><div class="ss">Room to scale.</div></div>
<div class="sx" style="border-color:var(--g)"><div class="sl2">Enjoy &amp; Grow</div><div class="sv" style="color:var(--g)">20%+</div><div class="ss">Before someone takes it.</div></div>
<div class="sx" style="border-color:var(--p)"><div class="sl2">Best Seen</div><div class="sv" style="color:var(--p)">42%</div><div class="ss">$2.2M &rarr; $840K</div></div></div></div>
<div class="cd"><div class="ct"><span class="ic ib">&#x2B07;</span> Sales Funnel</div><div class="fn" id="gwyw-sfun"></div></div>
<div class="g2">
<div class="cd"><div class="ct"><span class="ic ig">&#x2713;</span> Calculated Results</div>
<div class="ig2"><label>Total Leads Needed / Year</label><input type="text" id="gwyw-ltot" readonly style="color:var(--o);background:rgba(251,146,60,.08);border-color:var(--o)"></div>
<div class="ig2"><label>Labor ($/sqft)</label><input type="text" id="gwyw-lpsf" value="$0.83" readonly style="color:var(--o);background:rgba(251,146,60,.08);border-color:var(--o)"></div>
<div class="ig2"><label>Drive Time ($/sqft)</label><input type="text" id="gwyw-dpsf" readonly style="color:var(--o);background:rgba(251,146,60,.08);border-color:var(--o)"></div>
</div>
<div class="cd"><div class="ct"><span class="ic iy">&#x1F4CB;</span> Weekly Targets</div>
<div id="gwyw-acctChart"></div></div>
</div>
<div class="cd"><div class="ct"><span class="ic io">&#x1F4E1;</span> Leading Indicators &mdash; Track These Daily &amp; Weekly</div>
<div class="sg" id="gwyw-leadingHero"></div>
<div class="qb"><div class="qt">"If I don't get eight clients today, and I only got seven, I could probably get nine tomorrow. But if I go a whole month and I miss them, I can't make up 160 clients in a day."</div><div class="qa">&mdash; Joe Quick</div></div>
</div>
<div class="g2">
<div class="cd"><div class="ct"><span class="ic ip">&#x1F4B0;</span> Marketing Metrics</div><div id="gwyw-mktM"></div></div>
<div class="cd"><div class="ct"><span class="ic io">&#x1F4E1;</span> Lead Source Mix</div><div class="lsb" id="gwyw-lsBar"></div><div id="gwyw-lsDet" style="overflow-x:auto"></div></div>
</div>
</div>

<div class="sec" id="s-proj">
<div class="sh"><div class="step-label">Proof of Work</div><h2>Project Model: <span id="gwyw-psn">Graniflex Floor System</span></h2><p>The unit economics of a single job. This is the math behind every dollar.</p></div>
<div class="pm" id="gwyw-psfM"></div>
<div class="sg" id="gwyw-pSt"></div>
</div>

<div class="sec" id="s-labor">
<div class="sh"><div class="step-label">Proof of Work</div><h2>Labor &amp; Equipment Detail: <span id="gwyw-lsn">G-301: Graniflex Flake</span></h2><p>Step-by-step labor breakdown on <span id="gwyw-labSqft">576</span> sq ft base. Equipment comparison shows ROI of upgrading machines.</p></div>
<div class="cd"><div class="ct"><span class="ic ig">&#x2713;</span> Labor Summary</div><div id="gwyw-lSum"></div></div>
<div class="cd"><div class="ct"><span class="ic ib">&#x1F4CB;</span> Step-by-Step Breakdown (<span id="gwyw-labSqft2">576</span> sq ft base)</div>
<div style="overflow-x:auto"><table class="dt" id="gwyw-lTable"><thead id="gwyw-lTH"></thead><tbody id="gwyw-lSB"></tbody></table></div></div>
<div class="cd"><div class="ct"><span class="ic io">&#x23F1;</span> Equipment Run Time</div><div id="gwyw-eqR"></div></div>
<div class="cd"><div class="ct"><span class="ic ip">&#x1F4CA;</span> Annual Machine Comparison</div>
<div class="eq-ctx" id="gwyw-eqCtx"></div>
<p style="font-size:.75rem;color:var(--t3);margin-bottom:12px" id="gwyw-eqNote">Machine run time multiplied by all workers on jobsite.</p>
<div style="overflow-x:auto"><table class="dt"><thead><tr><th>Equipment</th><th>Sq Ft/Hr</th><th>Hrs to Grind</th><th>Hrs w/ Removal</th><th>Yearly Grind Time</th><th>Yearly Removal Time</th><th>Yearly Labor Cost</th></tr></thead><tbody id="gwyw-eqCB"></tbody></table></div></div>
</div>

<div class="sec" id="s-tgt">
<div class="sh"><div class="step-label">Proof of Work</div><h2>Target Area Scenarios</h2><p>Compare project types. How many project jobs does it take?</p></div>
<div class="qb"><div class="qt">"Doing more doesn't get you more. Doing better gets you more."</div><div class="qa">&mdash; Joe Quick</div></div>
<div class="cd"><div style="overflow-x:auto"><table class="dt"><thead><tr><th>Target Area</th><th>Sq Ft</th><th>@ $6.50/ft</th><th class="gwyw-jth">Jobs</th><th>@ $8.00/ft</th><th class="gwyw-jth">Jobs</th><th>@ $9.60/ft</th><th class="gwyw-jth">Jobs</th></tr></thead><tbody id="gwyw-tCB"></tbody></table></div></div>
</div>

</div>
</div>

<script>
(function(){
var gR={};
var SYS={
  graniflex:{name:'Graniflex Floor System',lname:'G-301: Graniflex Flake: Perfect Poly 90: 1 Coat',mat:2.65,price:8.00,baseGrindRate:500,
    steps:[{desc:'Setup',hrs:0.5},{desc:'Grind / Blast',hrs:1.5,grind:true},{desc:'Repairs',hrs:0.5},{desc:'Prime with Permaflex',hrs:1},{desc:'Coat with Permaflex, Broadcast Media',hrs:1},{desc:'Clean and Seal with PP90 (1 and Done)',hrs:1.5}]},
  rcw_ext:{name:'Rustic Concrete Wood (Exterior)',lname:'Rustic Concrete Wood: Exterior Application',mat:1.15,price:8.00,baseGrindRate:500,
    steps:[{desc:'Setup',hrs:0.5},{desc:'Grind / Blast',hrs:1.5,grind:true},{desc:'Repairs',hrs:0.5},{desc:'Grout Coat w/ High Density Resin + Texture Mix',hrs:1},{desc:'Tape and Texture Coat',hrs:2},{desc:'Stain',hrs:1.5},{desc:'Acrylic Seal Coat 1',hrs:1},{desc:'Acrylic Seal Coat 2',hrs:1}]}
};
var PRE={garage:576,basement:1200,pool:1500,driveway:1800,firestation:5000,walmart:200000,factory:100000};
var MACH=[{name:'2047.4H',sqfthr:500},{name:'Samson 2756',sqfthr:800},{name:'Leonidas 2795',sqfthr:1200},{name:'Leonidas 2795P',sqfthr:2000}];
var TGT=[{name:'Garage',sqft:576},{name:'Basement',sqft:1200},{name:'Pool Deck',sqft:1500},{name:'Driveway',sqft:1800},{name:'Fire Station',sqft:5000},{name:'Walmart',sqft:200000},{name:'Factory',sqft:100000}];
var cs='<?php echo esc_js($s['product_system']); ?>';
var crew=<?php echo $crew_json; ?>;

var gEl=function(id){return document.getElementById('gwyw-'+id);};
var n=function(id){return parseFloat(gEl(id).value)||0;};
var f=function(v,d){d=d||0;return v.toLocaleString('en-US',{minimumFractionDigits:d,maximumFractionDigits:d});};
var fm=function(v){return '$'+f(v);};
var fm2=function(v){return '$'+f(v,2);};
var fp=function(v,d){d=d===undefined?1:d;return f(v,d)+'%';};

function renderCrew(){
  var h='<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(100px,1fr));gap:6px">';
  crew.forEach(function(r,i){h+='<div class="ig2" style="margin:0"><label style="font-size:.65rem">Tech '+(i+1)+' $/hr</label><input type="number" id="gwyw-cr'+i+'" value="'+r+'" class="ed" style="padding:6px 8px" oninput="gwyw_crewChange('+i+',this.value)"></div>';});
  h+='</div>';gEl('crewInputs').innerHTML=h;gEl('crewCount').textContent=crew.length+' techs';gEl('rmBtn').style.display=crew.length>1?'':'none';
}

function go(id,e){
  var root=document.getElementById('gwyw-calc');
  root.querySelectorAll('.sec').forEach(function(s){s.classList.remove('ac');});
  root.querySelectorAll('.nb').forEach(function(b){b.classList.remove('ac');});
  document.getElementById('s-'+id).classList.add('ac');
  e.target.closest('.nb').classList.add('ac');
}

function onSys(){cs=gEl('ps').value;var s=SYS[cs];gEl('cog').value=s.mat;gEl('psf').value=s.price;gEl('psn').textContent=s.name;gEl('lsn').textContent=s.lname;calc();}
function preset(){var v=gEl('tat').value;if(PRE[v])gEl('sqft').value=PRE[v];calc();}
function addTech(){crew.push(15);renderCrew();calc();}
function removeTech(){if(crew.length>1){crew.pop();renderCrew();calc();}}
function crewChange(i,v){crew[i]=parseFloat(v)||0;calc();}

function calc(){
  var sys=SYS[cs],sqft=n('sqft'),price=n('psf'),mat=n('cog'),rep=n('rep'),opPct=n('opc')/100;
  var N=crew.length;
  var rates=crew.map(function(_,i){return parseFloat((gEl('cr'+i)||{}).value)||crew[i];});
  var avgHr=rates.reduce(function(a,b){return a+b;},0)/N;
  var tgp=n('tgp'),wwy=n('wwy')||42,lcr=n('lcr')/100,ccr=n('ccr')/100;
  var mkp=n('mkp')/100,bep=n('bep')/100,scp=n('scp2')/100;

  var eqS=gEl('eqs'),eqSqftHr=parseInt(eqS.options[eqS.selectedIndex].getAttribute('data-sqfthr'));
  var eqName=eqS.options[eqS.selectedIndex].getAttribute('data-name');
  var BASE_SQFT=576,grindRatio=sys.baseGrindRate/eqSqftHr,driveHrs=n('dth');

  var techProdHrs=new Array(N).fill(0);var stepData=[];
  sys.steps.forEach(function(s){
    var mult=s.grind?grindRatio:1,hpt=s.hrs*mult,th=new Array(N).fill(hpt);
    th.forEach(function(h,i){techProdHrs[i]+=h;});
    stepData.push({desc:s.grind?s.desc+' ('+eqName+')':s.desc,techHrs:th,totalHrs:hpt*N,psfCost:hpt*N*avgHr/BASE_SQFT});
  });
  var techDriveHrs=new Array(N).fill(driveHrs),techTotalHrs=techProdHrs.map(function(h){return h+driveHrs;});
  var dTot=driveHrs*N,prodTot=techProdHrs.reduce(function(a,b){return a+b;},0),gTot=prodTot+dTot;
  var subLC=techProdHrs.reduce(function(a,h,i){return a+h*rates[i];},0),drvC=techDriveHrs.reduce(function(a,h,i){return a+h*rates[i];},0),totLC=subLC+drvC;
  var labPsf=subLC/BASE_SQFT;

  var gs=sqft*price,cogT=sqft*mat,labT=sqft*labPsf,opPsf=price*opPct,opT=sqft*opPsf;
  var gpPsf=price-mat-labPsf-opPsf,gpT=gs+rep-cogT-labT-opT,gpM=gs>0?(gpT/(gs+rep))*100:0;

  var jobsX=gpT>0?tgp/gpT:0,jobsN=Math.round(jobsX),ySqft=Math.round(jobsX*sqft);
  var tGS=jobsX*(gs+rep),tCOG=jobsX*cogT,tLab=jobsX*labT,tOp=tGS*opPct;
  var aGP=tGS-tCOG-tLab-tOp,gpPc=tGS>0?(aGP/tGS)*100:0;
  var mC=tGS*mkp,bC=tGS*bep,dC=drvC*jobsX,sC=tGS*scp;
  var nP=aGP-mC-bC-dC-sC,nPc=tGS>0?(nP/tGS)*100:0;
  var pCol=nPc>=20?'var(--g)':nPc>=15?'var(--y)':nPc>=10?'var(--o)':'var(--r)';
  var pRule=nPc>=20?'ENJOY & GROW FAST':nPc>=15?'TIME TO GROW':nPc>=10?'STOP GROWING':'DANGER';

  var quotes=ccr>0?Math.ceil(jobsX/ccr):0;
  var totalLeads=lcr>0?Math.ceil(quotes/lcr):0;
  var contracts=jobsN;
  var jpw=wwy>0?jobsX/wwy:0;
  var leadsWk=wwy>0?totalLeads/wwy:0,quotesWk=wwy>0?quotes/wwy:0,leadsDay=leadsWk/5;
  var mktTotal=tGS*mkp,cpl=totalLeads>0?mktTotal/totalLeads:0,cpq=quotes>0?mktTotal/quotes:0,cac=contracts>0?mktTotal/contracts:0;

  var sp1=n('sp1'),sp2=n('sp2'),sp3=n('sp3'),sp4=n('sp4'),sp5=n('sp5');
  var spSum=sp1+sp2+sp3+sp4+sp5;
  var srcPcts=[sp1,sp2,sp3,sp4,sp5];
  var srcCounts=srcPcts.map(function(p){return spSum>0?Math.round(totalLeads*p/spSum):0;});

  var tech1TotalHrs=techTotalHrs[0]||0,tech1Lab=jobsX*(tech1TotalHrs*rates[0]);
  var inBiz=tech1Lab+sC,onBiz=nP,owT=inBiz+onBiz;

  var baseGrindManHrs=1.5*N,curGrindManHrs=1.5*grindRatio*N;
  var costSaved=(baseGrindManHrs-curGrindManHrs)*avgHr,costSavedYr=costSaved*jobsX;

  // === RENDER ===
  gEl('lpsf').value=fm2(labPsf)+'/ft';
  gEl('dpsf').value=fm2(drvC/BASE_SQFT)+'/ft';
  gEl('ltot').value=f(totalLeads)+' leads needed';
  gEl('projNeeded').textContent=f(jobsN);
  gEl('projPerWk').textContent=f(jpw,2)+' / week';
  gEl('labSqft').textContent=f(sqft);
  gEl('labSqft2').textContent=f(sqft);

  var arrow='<span style="color:var(--t3);font-size:1.2rem;padding:0 6px">\u2192</span>';
  var chainBox=function(label,value,color){return '<div style="text-align:center;padding:6px 14px"><div style="font-size:.6rem;font-weight:600;letter-spacing:.8px;text-transform:uppercase;color:var(--t3)">'+label+'</div><div style="font-family:\'JetBrains Mono\',monospace;font-size:1.1rem;font-weight:700;color:'+color+'">'+value+'</div></div>';};
  gEl('revChain').innerHTML=chainBox('GP Target',fm(tgp),'var(--y)')+arrow+chainBox('\u00f7 '+fm(gpT)+'/job','','var(--t3)')+arrow+chainBox('Projects',f(jobsN),'var(--g)')+arrow+chainBox('\u00f7 '+fp(ccr*100,0)+' close','','var(--t3)')+arrow+chainBox('Quotes',f(quotes),'var(--b)')+arrow+chainBox('\u00f7 '+fp(lcr*100,0)+' conv','','var(--t3)')+arrow+chainBox('Leads',f(totalLeads),'var(--o)');
  var spTotEl=gEl('spTot');spTotEl.value=f(spSum)+'%';
  spTotEl.style.color=spSum===100?'var(--g)':spSum>100?'var(--r)':'var(--o)';
  spTotEl.style.background=spSum===100?'rgba(52,211,153,.08)':'rgba(248,113,113,.08)';
  spTotEl.style.borderColor=spSum===100?'var(--g)':'var(--r)';

  gEl('ownerV').innerHTML='<h3>SHAREHOLDERS VISION = ROI OF TIME, TALENT &amp; TREASURE</h3><div class="hero-total" style="border-top:none;padding-top:0;margin-top:0;justify-content:center"><span class="vv" style="color:var(--y);font-size:2rem">'+fm2(owT)+'</span></div><div style="text-align:center;font-size:.75rem;color:var(--t3);margin:4px 0 14px">'+fm(owT/12)+' / month</div><div class="vr"><span class="vl2">In The Business Labor (Tech 1: '+f(jobsN)+' jobs \u00d7 '+f(tech1TotalHrs,1)+' hrs \u00d7 $'+f(rates[0])+')</span><span class="vv" style="color:var(--o)">'+fm2(tech1Lab)+'</span></div><div class="vr"><span class="vl2">Sales Commission ('+fp(scp*100,0)+' of '+fm(tGS)+')</span><span class="vv" style="color:var(--o)">'+fm2(sC)+'</span></div><div class="vr" style="border-top:2px solid var(--bd2);margin-top:6px;padding-top:8px"><span class="vl2" style="font-weight:700">Total Working In The Business</span><span class="vv" style="color:var(--o)">'+fm2(inBiz)+'</span></div><div class="vr" style="margin-top:10px"><span class="vl2" style="font-weight:700">Total Working On The Business (Net Profit)</span><span class="vv" style="color:var(--g)">+ '+fm2(onBiz)+'</span></div><div class="vr" style="border-top:3px solid var(--y);margin-top:8px;padding-top:10px"><span class="vl2" style="font-weight:700;color:var(--y);font-size:.95rem">'+fm2(inBiz)+' + '+fm2(onBiz)+'</span><span class="vv" style="color:var(--y);font-size:1.2rem">= '+fm2(owT)+'</span></div>';

  gEl('acctChart').innerHTML='<div class="sg" style="margin-bottom:0"><div class="sx" style="border-color:var(--o)"><div class="sl2">Marketing</div><div class="sv" style="color:var(--o)">'+f(leadsWk,1)+'</div><div class="ss">Leads / Week ('+f(totalLeads)+' / yr)</div></div><div class="sx" style="border-color:var(--b)"><div class="sl2">Sales</div><div class="sv" style="color:var(--b)">'+f(quotesWk,1)+'</div><div class="ss">Quotes / Week ('+f(quotes)+' / yr)</div></div><div class="sx" style="border-color:var(--g)"><div class="sl2">Operations</div><div class="sv" style="color:var(--g)">'+f(jpw,2)+'</div><div class="ss">Jobs / Week ('+f(jobsN)+' / yr)</div></div><div class="sx" style="border-color:var(--y)"><div class="sl2">Finance</div><div class="sv" style="color:var(--y)">'+fp(nPc)+'</div><div class="ss">'+pRule+'</div></div></div>';

  gEl('leadingHero').innerHTML='<div class="sx" style="border-color:var(--o);border-width:2px"><div class="sl2">Leads / Week</div><div class="sv" style="color:var(--o)">'+f(leadsWk,1)+'</div><div class="ss">'+f(totalLeads)+' / year</div></div><div class="sx" style="border-color:var(--o);border-width:2px"><div class="sl2">Leads / Day</div><div class="sv" style="color:var(--o);font-size:2rem">'+f(leadsDay,1)+'</div><div class="ss">TRACK THIS DAILY</div></div><div class="sx" style="border-color:var(--b);border-width:2px"><div class="sl2">Quotes / Week</div><div class="sv" style="color:var(--b)">'+f(quotesWk,1)+'</div><div class="ss">'+f(quotes)+' / year</div></div><div class="sx" style="border-color:var(--y);border-width:2px"><div class="sl2">Contracts / Week</div><div class="sv" style="color:var(--y)">'+f(jpw,2)+'</div><div class="ss">'+f(jobsN)+' / year</div></div>';

  var fD=[{l:'Target Gross Profit',v:tgp,c:'var(--g)',p:15,m:true},{l:'Projects Needed ('+f(jobsN)+'/yr)',v:jobsN,c:'var(--y)',p:totalLeads>0?(contracts/totalLeads)*100:20},{l:'Design Consultations Needed (\u00f7 '+fp(ccr*100,0)+' close)',v:quotes,c:'var(--b)',p:totalLeads>0?(quotes/totalLeads)*100:40},{l:'Lead Opportunities Needed (\u00f7 '+fp(lcr*100,0)+' conv)',v:totalLeads,c:'var(--p)',p:100}];
  var fH='';fD.forEach(function(x,i){var w=Math.max(x.p,20);fH+='<div class="fs"><div class="fb" style="width:'+w+'%;background:'+x.c+'"></div><span class="fl">'+x.l+'</span><span class="fv" style="color:'+x.c+'">'+(x.m?fm(x.v):f(x.v))+'</span>'+(i<fD.length-1?'<span class="fa">\u25BC</span>':'')+'</div>';});gEl('sfun').innerHTML=fH;

  gEl('mktM').innerHTML='<div class="rr"><span class="lb">Marketing Budget ('+fp(mkp*100,0)+' of Gross)</span><span class="vl" style="color:var(--r)">'+fm2(mktTotal)+'</span></div><div class="rr"><span class="lb">Cost Per Lead</span><span class="vl" style="color:var(--o)">'+fm2(cpl)+'</span></div><div class="rr"><span class="lb">Cost Per Quote</span><span class="vl" style="color:var(--o)">'+fm2(cpq)+'</span></div><div class="rr tot"><span class="lb">Customer Acquisition Cost</span><span class="vl" style="color:var(--r)">'+fm2(cac)+'</span></div>';

  var srcNames=['Inbound Calls','Website Forms','Mailers','Referrals','Repeat'];
  var sCol=['#f87171','#60a5fa','#f5c518','#34d399','#a78bfa'];var bH='',dH='<table class="dt"><thead><tr><th>Source</th><th>%</th><th>Leads/Yr</th><th>Leads/Wk</th></tr></thead><tbody>';
  srcNames.forEach(function(nm,i){var pct=srcPcts[i],ct=srcCounts[i],wk=wwy>0?ct/wwy:0;
    bH+='<div class="seg" style="flex:'+pct+';background:'+sCol[i]+'">'+(pct>8?f(pct,0)+'%':'')+'</div>';
    dH+='<tr><td><span style="display:inline-block;width:8px;height:8px;border-radius:2px;background:'+sCol[i]+';margin-right:6px;vertical-align:middle"></span>'+nm+'</td><td class="mn">'+f(pct)+'%</td><td class="mn">'+f(ct)+'</td><td class="mn">'+f(wk,1)+'</td></tr>';});
  dH+='</tbody></table>';gEl('lsBar').innerHTML=bH;gEl('lsDet').innerHTML=dH;

  gEl('pnlS').innerHTML='<div class="sx"><div class="sl2">Gross Sales: Vanity</div><div class="sv" style="color:var(--g)">'+fm(tGS)+'</div></div><div class="sx"><div class="sl2">Net Profit: Sanity</div><div class="sv" style="color:'+pCol+'">'+fm(nP)+'</div></div><div class="sx"><div class="sl2">Net Margin</div><div class="sv" style="color:'+pCol+'">'+fp(nPc)+'</div><div class="ss">'+pRule+'</div></div><div class="sx"><div class="sl2">Projects</div><div class="sv" style="color:var(--b)">'+f(jobsN)+'</div><div class="ss">'+f(sqft)+' sq ft each</div></div><div class="sx"><div class="sl2">Sq Ft / Year</div><div class="sv" style="color:var(--p)">'+f(ySqft)+'</div></div>';
  gEl('pnlR').innerHTML='<div class="rr"><span class="lb">Gross Sales ('+jobsN+' projects)</span><span class="vl pr">'+fm(tGS)+'</span></div><div class="rr"><span class="lb">Cost of Goods ('+fp(tGS>0?(tCOG/tGS)*100:0)+')</span><span class="vl pc">\u2212'+fm(tCOG)+'</span></div><div class="rr"><span class="lb">Labor \u2014 '+N+' techs ('+fp(tGS>0?(tLab/tGS)*100:0)+')</span><span class="vl pc">\u2212'+fm(tLab)+'</span></div><div class="rr"><span class="lb">Operations ('+fp(opPct*100,0)+')</span><span class="vl pc">\u2212'+fm(tOp)+'</span></div><div class="rr tot"><span class="lb">Gross Profit ('+fp(gpPc)+')</span><span class="vl pp">'+fm(aGP)+'</span></div><div class="rr"><span class="lb">Marketing ('+fp(mkp*100,0)+')</span><span class="vl pc">\u2212'+fm(mC)+'</span></div><div class="rr"><span class="lb">Business Expense ('+fp(bep*100,0)+')</span><span class="vl pc">\u2212'+fm(bC)+'</span></div><div class="rr"><span class="lb">Driving Labor ('+f(driveHrs,1)+' hrs/tech \u00d7 '+N+')</span><span class="vl pc">\u2212'+fm(dC)+'</span></div><div class="rr"><span class="lb">Sales Commission ('+fp(scp*100,0)+')</span><span class="vl pc">\u2212'+fm(sC)+'</span></div><div class="rr tot"><span class="lb">Net Profit = Sanity = ROI ('+fp(nPc)+')</span><span class="vl '+(nP>=0?'pr':'pc')+'">'+fm(nP)+'</span></div>';

  gEl('psfM').innerHTML='<div class="pt">'+sys.name.toUpperCase()+' \u2014 '+f(sqft)+' SQ FT \u2014 '+N+' TECHS \u2014 '+eqName+'</div>'+'<div class="pr2 ph"><span class="pl"></span><span class="pp2">PSF</span><span class="pt2">TOTAL</span></div>'+'<div class="pr2"><span class="pl">Gross Sales: Charge to Customer</span><span class="pp2" style="color:var(--g)">'+fm2(price)+'</span><span class="pt2" style="color:var(--g)">'+fm2(gs)+'</span></div>'+(rep>0?'<div class="pr2"><span class="pl">Repair Charges</span><span class="pp2"></span><span class="pt2" style="color:var(--g)">'+fm2(rep)+'</span></div>':'')+'<div class="pr2"><span class="pl">Cost of Goods</span><span class="pp2" style="color:var(--r)">'+fm2(mat)+'</span><span class="pt2" style="color:var(--r)">'+fm2(cogT)+'</span></div>'+'<div class="pr2"><span class="pl">Labor ('+N+' techs)</span><span class="pp2" style="color:var(--o)">'+fm2(labPsf)+'</span><span class="pt2" style="color:var(--o)">'+fm2(labT)+'</span></div>'+'<div class="pr2"><span class="pl">Operating Cost @ '+fp(opPct*100,0)+'</span><span class="pp2" style="color:var(--r)">'+fm2(opPsf)+'</span><span class="pt2" style="color:var(--r)">'+fm2(opT)+'</span></div>'+'<div class="pr2 pgp"><span class="pl">Gross Profit</span><span class="pp2" style="color:var(--y)">'+fm2(gpPsf)+'</span><span class="pt2" style="color:var(--y)">'+fm2(gpT)+'</span></div>'+'<div class="pr2"><span class="pl">Job Gross Profit Margin</span><span class="pp2"></span><span class="pt2" style="color:var(--y);font-size:1.05rem">'+fp(gpM,0)+'</span></div>';
  gEl('pSt').innerHTML='<div class="sx"><div class="sl2">Revenue</div><div class="sv" style="color:var(--g)">'+fm(gs+rep)+'</div></div><div class="sx"><div class="sl2">COGS</div><div class="sv" style="color:var(--r)">'+fm(cogT)+'</div><div class="ss">'+fp(gs>0?(cogT/gs)*100:0)+'</div></div><div class="sx"><div class="sl2">Labor</div><div class="sv" style="color:var(--o)">'+fm(labT)+'</div><div class="ss">'+fm2(labPsf)+'/ft \u2022 '+N+' techs</div></div><div class="sx"><div class="sl2">Gross Profit</div><div class="sv" style="color:var(--y)">'+fm(gpT)+'</div></div><div class="sx"><div class="sl2">GP Margin</div><div class="sv" style="color:var(--y)">'+fp(gpM,0)+'</div></div>';

  var thR='<tr><th>Step</th>';for(var i=0;i<N;i++) thR+='<th>Tech '+(i+1)+'</th>';thR+='<th>Total Hrs</th><th>Per Sq Ft</th></tr>';gEl('lTH').innerHTML=thR;
  var lR='';
  stepData.forEach(function(sd){lR+='<tr><td>'+sd.desc+'</td>';sd.techHrs.forEach(function(h){lR+='<td class="mn">'+f(h,2)+'</td>';});lR+='<td class="mn">'+f(sd.totalHrs,2)+'</td><td class="mn">'+fm2(sd.psfCost)+'</td></tr>';});
  lR+='<tr style="font-weight:700;border-top:2px solid var(--bd2)"><td>Total Production Hours</td>';techProdHrs.forEach(function(h){lR+='<td class="mn">'+f(h,2)+'</td>';});lR+='<td class="mn">'+f(prodTot,2)+'</td><td class="mn">'+fm2(subLC/BASE_SQFT)+'</td></tr>';
  lR+='<tr><td>SubTotal Labor Cost</td>';techProdHrs.forEach(function(h,i){lR+='<td class="mn">'+fm2(h*rates[i])+'</td>';});lR+='<td class="mn" style="color:var(--o)">'+fm2(subLC)+'</td><td class="mn">'+fm2(subLC/BASE_SQFT)+'</td></tr>';
  lR+='<tr><td>Drive Time / Visits</td>';techDriveHrs.forEach(function(h){lR+='<td class="mn">'+f(h,1)+'</td>';});lR+='<td class="mn">'+f(dTot,1)+'</td><td class="mn">'+fm2(drvC/BASE_SQFT)+'</td></tr>';
  lR+='<tr style="font-weight:700;border-top:2px solid var(--bd2)"><td>GRAND TOTAL</td>';techTotalHrs.forEach(function(h){lR+='<td class="mn">'+f(h,2)+'</td>';});lR+='<td class="mn">'+f(gTot,2)+'</td><td class="mn" style="color:var(--y)">'+fm2(totLC/BASE_SQFT)+'</td></tr>';
  lR+='<tr><td>Total Labor + Driving $</td>';techTotalHrs.forEach(function(h,i){lR+='<td class="mn">'+fm2(h*rates[i])+'</td>';});lR+='<td class="mn" style="color:var(--y)">'+fm2(totLC)+'</td><td class="mn">'+fm2(totLC/BASE_SQFT)+'</td></tr>';
  lR+='<tr><td>Each Man Cost / Sq Ft</td>';techTotalHrs.forEach(function(h,i){lR+='<td class="mn">'+fm2(h*rates[i]/BASE_SQFT)+'</td>';});lR+='<td></td><td></td></tr>';
  gEl('lSB').innerHTML=lR;

  var savingsRow=grindRatio<1?'<div class="rr" style="background:rgba(52,211,153,.08);border-radius:6px;padding:9px 12px;margin-top:4px"><span class="lb" style="color:var(--g)">'+eqName+' Saves vs 2047.4H</span><span class="vl" style="color:var(--g)">\u2212'+fm2(costSaved)+'/job \u2022 \u2212'+fm(costSavedYr)+'/yr</span></div>':'';
  gEl('lSum').innerHTML='<div class="rr"><span class="lb">Crew Size</span><span class="vl" style="color:var(--t)">'+N+' techs</span></div><div class="rr"><span class="lb">Equipment</span><span class="vl" style="color:var(--t)">'+eqName+' ('+f(eqSqftHr)+' sqft/hr)</span></div><div class="rr"><span class="lb">Average Man Hour Rate</span><span class="vl" style="color:var(--y)">'+fm2(avgHr)+'</span></div><div class="rr"><span class="lb">Labor $/Sq Ft</span><span class="vl" style="color:var(--o)">'+fm2(labPsf)+'</span></div><div class="rr"><span class="lb">This Project ('+f(sqft)+' sq ft)</span><span class="vl" style="color:var(--o)">'+fm(labT)+'</span></div><div class="rr"><span class="lb">Grand Total w/ Driving (576 base)</span><span class="vl" style="color:var(--y)">'+fm(totLC)+'</span></div>'+savingsRow;

  var rm=gEl('rmv').value==='yes',gh=eqSqftHr>0?sqft/eqSqftHr:0,tgh=rm?gh*2:gh;
  gEl('eqR').innerHTML='<div class="rr"><span class="lb">Quantity</span><span class="vl" style="color:var(--t)">'+f(sqft)+' sq ft</span></div><div class="rr"><span class="lb">Sq Ft/Hr</span><span class="vl" style="color:var(--b)">'+f(eqSqftHr)+'</span></div><div class="rr"><span class="lb">Hours to Grind</span><span class="vl" style="color:var(--y)">'+f(gh,2)+'</span></div>'+(rm?'<div class="rr"><span class="lb">Hours w/ Removal (2x)</span><span class="vl" style="color:var(--o)">'+f(tgh,2)+'</span></div>':'');
  gEl('eqCtx').innerHTML='<div class="ec-item"><span class="ec-label">Quantity</span><span class="ec-val">'+f(sqft)+' sq ft</span></div><div class="ec-item"><span class="ec-label">Sq Ft / Year</span><span class="ec-val">'+f(ySqft)+'</span></div><div class="ec-item"><span class="ec-label">Projects</span><span class="ec-val">'+f(jobsN)+'</span></div><div class="ec-item"><span class="ec-label">Crew</span><span class="ec-val">'+N+' techs</span></div>';
  gEl('eqNote').textContent='Machine run time multiplied by all '+N+' workers on jobsite.';
  var eqH='';MACH.forEach(function(m){var h=sqft/m.sqfthr,hr=h*2,yg=ySqft/m.sqfthr,yr=yg*2,lc=yg*avgHr*N;
    eqH+='<tr><td>'+m.name+'</td><td class="mn">'+f(m.sqfthr)+'</td><td class="mn">'+f(h,2)+'</td><td class="mn">'+f(hr,2)+'</td><td class="mn">'+f(yg,2)+'</td><td class="mn">'+f(yr,2)+'</td><td class="mn" style="color:var(--y)">'+fm2(lc)+'</td></tr>';});
  gEl('eqCB').innerHTML=eqH;

  var tLbl='Jobs for '+fm(tgp);document.querySelectorAll('.gwyw-jth').forEach(function(el){el.textContent=tLbl;});
  var pT=[6.50,8.00,9.60];var tRw='';TGT.forEach(function(t){tRw+='<tr><td>'+t.name+'</td><td class="mn">'+f(t.sqft)+'</td>';pT.forEach(function(p){var rev=t.sqft*p,mt=t.sqft*mat,lb=t.sqft*labPsf,op=rev*opPct,gp=rev-mt-lb-op;var j=gp>0?Math.ceil(tgp/gp):'\u2014';tRw+='<td class="mn">'+fm(rev)+'</td><td class="mn" style="color:var(--y)">'+j+'</td>';});tRw+='</tr>';});gEl('tCB').innerHTML=tRw;

  gR={sysName:sys.name,sqft:sqft,price:price,mat:mat,N:N,eqName:eqName,tgp:tgp,wwy:wwy,jobsN:jobsN,jpw:jpw,tGS:tGS,tCOG:tCOG,tLab:tLab,tOp:tOp,aGP:aGP,gpPc:gpPc,mC:mC,bC:bC,dC:dC,sC:sC,nP:nP,nPc:nPc,pRule:pRule,totalLeads:totalLeads,quotes:quotes,contracts:contracts,leadsWk:leadsWk,quotesWk:quotesWk,leadsDay:leadsDay,cpl:cpl,cpq:cpq,cac:cac,labPsf:labPsf,avgHr:avgHr,rates:rates,gs:gs,rep:rep,cogT:cogT,labT:labT,opT:opT,gpT:gpT,gpM:gpM,opPct:opPct*100,mkp:mkp*100,bep:bep*100,scp:scp*100,ccr:ccr*100,lcr:lcr*100,owT:owT,inBiz:inBiz,onBiz:onBiz,srcNames:['Inbound Calls','Website Forms','Mailers','Referrals','Repeat'],srcPcts:srcPcts,srcCounts:srcCounts,eqSqftHr:eqSqftHr,stepData:stepData,techProdHrs:techProdHrs,prodTot:prodTot,drvC:drvC,totLC:totLC,driveHrs:driveHrs,BASE_SQFT:BASE_SQFT};
}

// Apply admin defaults for product system
if(cs!=='graniflex'){gEl('ps').value=cs;onSys();}
renderCrew();calc();

function generatePDF(){
  var jsPDF=window.jspdf.jsPDF;
  var doc=new jsPDF({unit:'pt',format:'letter'});
  var W=612,H=792,mx=40,cw=W-mx*2;
  var y=0,pg=1;
  var R=gR;

  var bg=[15,17,23],c1=[24,27,36],bd=[42,47,62],gold=[245,197,24],wh=[232,234,240],
      dim=[139,146,165],dim2=[90,97,120],grn=[52,211,153],red=[248,113,113],
      blu=[96,165,250],ora=[251,146,60];

  function newPage(){doc.addPage();pg++;y=40;drawPageBg();}
  function check(need){if(y+need>H-50)newPage();}
  function drawPageBg(){doc.setFillColor(bg[0],bg[1],bg[2]);doc.rect(0,0,W,H,'F');}

  function section(title){
    check(50);
    doc.setFillColor(c1[0],c1[1],c1[2]);doc.roundedRect(mx-4,y-2,cw+8,28,4,4,'F');
    doc.setFontSize(13);doc.setTextColor(gold[0],gold[1],gold[2]);doc.text(title.toUpperCase(),mx+8,y+17);
    doc.setDrawColor(gold[0],gold[1],gold[2]);doc.setLineWidth(1.5);doc.line(mx,y+30,mx+cw,y+30);
    y+=40;
  }

  function row(label,value,opts){
    opts=opts||{};check(20);
    var lc=opts.labelColor||dim,vc=opts.valueColor||wh;
    doc.setFontSize(9);doc.setTextColor(lc[0],lc[1],lc[2]);doc.text(label,mx+8,y+12);
    doc.setFontSize(10);doc.setTextColor(vc[0],vc[1],vc[2]);doc.text(value,mx+cw-8,y+12,{align:'right'});
    if(!opts.noline){doc.setDrawColor(bd[0],bd[1],bd[2]);doc.setLineWidth(0.5);doc.line(mx+4,y+18,mx+cw-4,y+18);}
    y+=22;
  }

  function totRow(label,value,vc){
    vc=vc||gold;check(28);
    doc.setDrawColor(gold[0],gold[1],gold[2]);doc.setLineWidth(1);doc.line(mx+4,y,mx+cw-4,y);
    doc.setFontSize(10);doc.setTextColor(wh[0],wh[1],wh[2]);doc.text(label,mx+8,y+16);
    doc.setFontSize(12);doc.setTextColor(vc[0],vc[1],vc[2]);doc.text(value,mx+cw-8,y+16,{align:'right'});
    doc.line(mx+4,y+22,mx+cw-4,y+22);
    y+=30;
  }

  function tableHeader(cols,widths){
    check(24);
    doc.setFillColor(c1[0],c1[1],c1[2]);doc.rect(mx,y,cw,18,'F');
    doc.setFontSize(7);doc.setTextColor(dim2[0],dim2[1],dim2[2]);
    var cx=mx+6;
    cols.forEach(function(c,i){doc.text(c.toUpperCase(),cx,y+12);cx+=widths[i];});
    y+=22;
  }

  function tableRow(cols,widths,opts){
    opts=opts||{};check(18);
    if(opts.bg){doc.setFillColor(opts.bg[0],opts.bg[1],opts.bg[2]);doc.rect(mx,y-2,cw,16,'F');}
    var cx=mx+6;
    cols.forEach(function(c,i){
      doc.setFontSize(8.5);
      var tc=i===0?(opts.bold?wh:dim):(opts.valueColor||wh);
      doc.setTextColor(tc[0],tc[1],tc[2]);
      var align=i===0?'left':'right';
      var tx=i===0?cx:cx+widths[i]-12;
      doc.text(String(c),tx,y+10,{align:align});
      cx+=widths[i];
    });
    if(!opts.noline){doc.setDrawColor(42,47,62);doc.setLineWidth(0.3);doc.line(mx+4,y+14,mx+cw-4,y+14);}
    y+=18;
  }

  drawPageBg();
  doc.setFillColor(c1[0],c1[1],c1[2]);doc.rect(0,0,W,80,'F');
  doc.setDrawColor(gold[0],gold[1],gold[2]);doc.setLineWidth(2);doc.line(0,80,W,80);
  doc.setFontSize(26);doc.setTextColor(gold[0],gold[1],gold[2]);doc.text('GETTING WHAT YOU WANT',mx,42);
  doc.setFontSize(10);doc.setTextColor(dim[0],dim[1],dim[2]);doc.text('Business Growth Calculator \u2014 Full Report',mx,60);
  doc.setFontSize(8);doc.setTextColor(dim2[0],dim2[1],dim2[2]);
  var today=new Date().toLocaleDateString('en-US',{year:'numeric',month:'long',day:'numeric'});
  doc.text(today,W-mx,35,{align:'right'});
  doc.text('The Concrete Protector \u00B7 I-BOS System',W-mx,50,{align:'right'});
  y=100;

  doc.setFillColor(c1[0],c1[1],c1[2]);doc.roundedRect(mx,y,cw,60,6,6,'F');
  doc.setDrawColor(bd[0],bd[1],bd[2]);doc.roundedRect(mx,y,cw,60,6,6,'S');
  var cfgItems=[['PRODUCT',R.sysName],['SQ FT',f(R.sqft)],['CHARGE','$'+f(R.price,2)+'/ft'],['CREW',R.N+' techs'],['EQUIPMENT',R.eqName],['GP TARGET','$'+f(R.tgp)]];
  var cx2=mx+14,cy=y+18;
  cfgItems.forEach(function(item){doc.setFontSize(6);doc.setTextColor(dim2[0],dim2[1],dim2[2]);doc.text(item[0],cx2,cy);doc.setFontSize(9);doc.setTextColor(wh[0],wh[1],wh[2]);doc.text(item[1],cx2,cy+14);cx2+=cw/6-2;});
  y+=78;

  section("Shareholder's Vision \u2014 ROI of Time, Talent & Treasure");
  doc.setFillColor(24,27,36);doc.roundedRect(mx+cw/4,y-4,cw/2,36,6,6,'F');
  doc.setDrawColor(gold[0],gold[1],gold[2]);doc.roundedRect(mx+cw/4,y-4,cw/2,36,6,6,'S');
  doc.setFontSize(18);doc.setTextColor(gold[0],gold[1],gold[2]);doc.text(fm2(R.owT),W/2,y+16,{align:'center'});
  doc.setFontSize(7);doc.setTextColor(dim[0],dim[1],dim[2]);doc.text(fm(R.owT/12)+' / month',W/2,y+28,{align:'center'});
  y+=44;
  row('Working In The Business (Labor + Commission)',fm2(R.inBiz),{valueColor:ora});
  row('Working On The Business (Net Profit)',fm2(R.onBiz),{valueColor:grn});
  totRow('Total Owner Compensation',fm2(R.owT));

  section('P&L Scorecard \u2014 Annual Projection');
  row('Gross Sales ('+R.jobsN+' projects)',fm(R.tGS),{valueColor:grn});
  row('Cost of Goods ('+fp(R.tGS>0?(R.tCOG/R.tGS)*100:0)+')','\u2212'+fm(R.tCOG),{valueColor:red});
  row('Labor \u2014 '+R.N+' techs ('+fp(R.tGS>0?(R.tLab/R.tGS)*100:0)+')','\u2212'+fm(R.tLab),{valueColor:red});
  row('Operations ('+fp(R.opPct)+')','\u2212'+fm(R.tOp),{valueColor:red});
  totRow('Gross Profit ('+fp(R.gpPc)+')',fm(R.aGP));
  row('Marketing ('+fp(R.mkp)+')','\u2212'+fm(R.mC),{valueColor:red});
  row('Business Expense ('+fp(R.bep)+')','\u2212'+fm(R.bC),{valueColor:red});
  row('Driving Labor ('+f(R.driveHrs,1)+' hrs/tech \u00D7 '+R.N+')','\u2212'+fm(R.dC),{valueColor:red});
  row('Sales Commission ('+fp(R.scp)+')','\u2212'+fm(R.sC),{valueColor:red});
  var npColor=R.nPc>=20?grn:R.nPc>=15?gold:R.nPc>=10?ora:red;
  totRow('Net Profit ('+fp(R.nPc)+') \u2014 '+R.pRule,fm(R.nP),npColor);

  newPage();
  section('Project Model \u2014 '+R.sysName+' \u2014 '+f(R.sqft)+' Sq Ft');
  var pmW=[cw*0.50,cw*0.25,cw*0.25];
  tableHeader(['Item','Per Sq Ft','Total'],pmW);
  tableRow(['Gross Sales: Charge to Customer','$'+f(R.price,2),'$'+f(R.gs,2)],pmW,{valueColor:grn});
  if(R.rep>0)tableRow(['Repair Charges','','$'+f(R.rep,2)],pmW,{valueColor:grn});
  tableRow(['Cost of Goods','$'+f(R.mat,2),'$'+f(R.cogT,2)],pmW,{valueColor:red});
  tableRow(['Labor ('+R.N+' techs)','$'+f(R.labPsf,2),'$'+f(R.labT,2)],pmW,{valueColor:ora});
  tableRow(['Operating Cost @ '+fp(R.opPct),'$'+f(R.price*R.opPct/100,2),'$'+f(R.opT,2)],pmW,{valueColor:red});
  y+=4;
  tableRow(['GROSS PROFIT','$'+f(R.gpT/R.sqft,2),'$'+f(R.gpT,2)],pmW,{bold:true,valueColor:gold,bg:[30,34,46]});
  tableRow(['Job Gross Margin','',fp(R.gpM,0)],pmW,{bold:true,valueColor:gold});
  y+=10;

  section('Sales Funnel');
  var funnelData=[['Gross Profit Target',fm(R.tgp),gold],['Projects Needed ('+f(R.jobsN)+'/yr)','@ $'+f(R.gpT,2)+'/job GP',grn],['Quotes Needed (\u00F7 '+fp(R.ccr)+'% close rate)',f(R.quotes),blu],['Leads Needed (\u00F7 '+fp(R.lcr)+'% conversion)',f(R.totalLeads),ora]];
  funnelData.forEach(function(item){check(24);doc.setFontSize(9);doc.setTextColor(dim[0],dim[1],dim[2]);doc.text(item[0],mx+12,y+12);doc.setFontSize(11);doc.setTextColor(item[2][0],item[2][1],item[2][2]);doc.text(item[1],mx+cw-12,y+12,{align:'right'});y+=22;});
  y+=10;

  section('Weekly & Daily Targets');
  var tgtW=[cw*0.45,cw*0.25,cw*0.30];
  tableHeader(['Metric','Per Week','Per Year'],tgtW);
  tableRow(['Leads (Marketing)',f(R.leadsWk,1),f(R.totalLeads)],tgtW,{valueColor:ora});
  tableRow(['Leads Per Day',f(R.leadsDay,1),'TRACK DAILY'],tgtW,{valueColor:ora,bold:true});
  tableRow(['Quotes (Sales)',f(R.quotesWk,1),f(R.quotes)],tgtW,{valueColor:blu});
  tableRow(['Contracts (Operations)',f(R.jpw,2),f(R.jobsN)],tgtW,{valueColor:gold});
  y+=10;

  section('Marketing Metrics');
  row('Marketing Budget ('+fp(R.mkp)+' of Gross)',fm2(R.mC),{valueColor:red});
  row('Cost Per Lead',fm2(R.cpl),{valueColor:ora});
  row('Cost Per Quote',fm2(R.cpq),{valueColor:ora});
  totRow('Customer Acquisition Cost',fm2(R.cac),red);

  check(120);
  section('Lead Source Mix');
  var lsW=[cw*0.35,cw*0.15,cw*0.25,cw*0.25];
  tableHeader(['Source','%','Leads/Year','Leads/Week'],lsW);
  R.srcNames.forEach(function(nm,i){var pct=R.srcPcts[i],ct=R.srcCounts[i],wk=R.wwy>0?ct/R.wwy:0;tableRow([nm,f(pct)+'%',f(ct),f(wk,1)],lsW);});
  y+=10;

  check(100);
  section('Labor & Equipment Summary');
  row('Crew Size',R.N+' techs',{valueColor:[45,212,191]});
  row('Equipment',R.eqName+' ('+f(R.eqSqftHr)+' sqft/hr)',{valueColor:[45,212,191]});
  row('Average Man Hour Rate',fm2(R.avgHr),{valueColor:gold});
  row('Labor $/Sq Ft',fm2(R.labPsf),{valueColor:ora});
  row('Production Hours (576 base)',f(R.prodTot,2)+' hrs',{valueColor:wh});
  row('Driving Cost / Job',fm2(R.drvC),{valueColor:ora});
  totRow('Total Labor + Drive (576 base)',fm2(R.totLC));

  check(30+R.N*18);
  y+=6;
  doc.setFontSize(8);doc.setTextColor(dim2[0],dim2[1],dim2[2]);doc.text('CREW PAY RATES',mx+8,y+10);y+=16;
  R.rates.forEach(function(r,i){row('Tech '+(i+1),'$'+f(r,2)+'/hr',{valueColor:wh});});

  for(var p=1;p<=pg;p++){
    doc.setPage(p);
    doc.setFontSize(7);doc.setTextColor(dim2[0],dim2[1],dim2[2]);
    doc.text('Getting What You Want \u2014 Business Calculator Report',mx,H-20);
    doc.text('Page '+p+' of '+pg,W-mx,H-20,{align:'right'});
    doc.text('Generated '+today+' \u2014 joequick.com',W/2,H-20,{align:'center'});
  }
  doc.save('GWYW-Business-Report-'+new Date().toISOString().slice(0,10)+'.pdf');
}

// Expose to global scope for onclick handlers
window.gwyw_go=go;
window.gwyw_onSys=onSys;
window.gwyw_preset=preset;
window.gwyw_calc=calc;
window.gwyw_addTech=addTech;
window.gwyw_removeTech=removeTech;
window.gwyw_crewChange=crewChange;
window.gwyw_generatePDF=generatePDF;
})();
</script>
    <?php
    return ob_get_clean();
}
add_shortcode('gwyw_calculator', 'gwyw_calculator_shortcode');

// ============================================================
// ACTIVATION
// ============================================================

function gwyw_calculator_activate() {
    $page_check = get_page_by_title('Business Calculator');
    if (!$page_check) {
        wp_insert_post(array(
            'post_title'    => 'Business Calculator',
            'post_content'  => '[gwyw_calculator]',
            'post_status'   => 'publish',
            'post_type'     => 'page',
            'post_author'   => 1,
            'comment_status' => 'closed',
            'ping_status'   => 'closed'
        ));
    }
}
register_activation_hook(__FILE__, 'gwyw_calculator_activate');

function gwyw_calculator_admin_notice() {
    if (get_transient('gwyw_calculator_activated')) {
        echo '<div class="notice notice-success is-dismissible"><p><strong>Getting What You Want Calculator</strong> is now active! <a href="' . admin_url('admin.php?page=gwyw-settings') . '">Configure Settings</a></p></div>';
        delete_transient('gwyw_calculator_activated');
    }
}
add_action('admin_notices', 'gwyw_calculator_admin_notice');

function gwyw_calculator_set_transient() {
    set_transient('gwyw_calculator_activated', true, 5);
}
register_activation_hook(__FILE__, 'gwyw_calculator_set_transient');
