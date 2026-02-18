#!/usr/bin/env python3
"""Batch post Daily Manna entries: Dec 9, 2025 - Jan 4, 2026"""

import subprocess, json, time

WP_URL = "https://joequick.com/wp-json/wp/v2/posts"
USER = "joe.quick"
PASS = "A4eZRwAwtv1HN9gQz7pk3Yae"

def post_entry(date_str, title, html_content):
    payload = json.dumps({
        "title": title,
        "content": html_content,
        "status": "publish",
        "categories": [43],
        "author": 16,
        "date": date_str
    })
    proc = subprocess.run(
        ["curl", "-s", "-X", "POST", WP_URL,
         "-u", f"{USER}:{PASS}",
         "-H", "Content-Type: application/json",
         "-d", payload],
        capture_output=True, text=True, timeout=30
    )
    try:
        resp = json.loads(proc.stdout)
        return resp.get('id'), resp.get('link')
    except:
        return None, proc.stdout[:200]

def wp(paragraphs):
    """Build WordPress block content from list of (type, text) tuples."""
    blocks = []
    for item in paragraphs:
        if isinstance(item, str):
            blocks.append(f"<!-- wp:paragraph -->\n<p>{item}</p>\n<!-- /wp:paragraph -->")
        elif isinstance(item, tuple):
            kind, text = item
            if kind == 'h3':
                blocks.append(f'<!-- wp:heading {{"level":3}} -->\n<h3>{text}</h3>\n<!-- /wp:heading -->')
            elif kind == 'hr':
                blocks.append('<!-- wp:separator -->\n<hr class="wp-block-separator"/>\n<!-- /wp:separator -->')
            elif kind == 'p':
                blocks.append(f"<!-- wp:paragraph -->\n<p>{text}</p>\n<!-- /wp:paragraph -->")
    return "\n\n".join(blocks)

entries = []

# Dec 9
entries.append(("2025-12-09T06:00:00", "Just in From Moldova \u2013 December 9, 2025", wp([
    '<em>\u201cHaving a form of godliness, but denying the power thereof: from such turn away.\u201d</em> \u2014 <strong>2 Timothy 3:5</strong>',
    '<em>\u201cThis people draw near me with their mouth, and with their lips do honour me, but have removed their heart far from me\u2026\u201d</em> \u2014 <strong>Isaiah 29:13</strong>',
    'These two verses \u2014 spoken centuries apart \u2014 speak with one voice: <strong>It is possible to practice religion externally while being spiritually empty internally.</strong>',
    'In Isaiah 29:13, God exposes a people who say the right words but carry the wrong heart. Their lips move in worship, but their heart moves away from God. Their religion is polite, polished, and powerless.',
    'In 2 Timothy 3:5, Paul warns Timothy of a last-days danger: people who maintain the appearance of godliness \u2014 the prayers, the rituals, the Christian vocabulary \u2014 but deny the transforming power of the Holy Spirit. They have the right form, but no fire. They have the motions, but not the Master. They have the outline, but not the overflow.',
    '<strong>God is not impressed by religious performance \u2014 He is moved by a surrendered heart.</strong>',
    ('hr', ''),
    ('h3', 'King Saul'),
    'King Saul looked like a king, acted like a king, and performed the outward rituals of religion, but his heart was far from God. <strong>1 Samuel 15:22\u201323</strong> \u2014 Saul offered sacrifices, yet God rejected them because Saul\u2019s obedience and heart were missing. <strong>1 Samuel 16:7</strong> \u2014 God reminds Samuel: \u201cThe LORD looketh on the heart.\u201d Saul had the form \u2014 his title, robe, throne, and ceremonies \u2014 but he denied the power that comes from obedience and surrender. Outward religion cannot cover inward rebellion.',
    ('hr', ''),
    ('h3', 'The Pharisees'),
    'Jesus repeatedly confronted the Pharisees for practicing empty religion. <strong>Matthew 23:27\u201328</strong> \u2014 \u201cYe appear beautiful outward\u2026 but within are full of hypocrisy.\u201d They prayed, fasted, tithed, and taught the Law, yet they lacked spiritual power because their heart was not surrendered. Jesus quoted Isaiah 29:13 directly to describe them (Matthew 15:7\u20139). Their lips honored God \u2014 but their heart was far away.',
    '<strong>Religious performance without heart surrender produces no spiritual power.</strong> These verses call every believer to examine the source of their spiritual life: Do we have a form, or do we have the power? Do we worship with our lips, while our heart drifts? Do we obey out of habit, or out of love? True godliness is not the shape of a life \u2014 it is the Spirit in a life.',
])))

# Dec 10
entries.append(("2025-12-10T06:00:00", "Just in From Moldova \u2013 December 10, 2025", wp([
    '<em>\u201cThe mountains quake at him, and the hills melt\u2026 and the earth is burned at his presence\u2026\u201d</em> \u2014 <strong>Nahum 1:5</strong>',
    '<em>\u201cAnd I saw a great white throne, and him that sat on it, from whose face the earth and the heaven fled away\u2026\u201d</em> \u2014 <strong>Revelation 20:11</strong>',
    '<strong>The Majesty of God Causes Creation and Men to Tremble.</strong> In Nahum, even the mountains \u2014 the strongest, oldest structures on earth \u2014 quake and melt when God arises in judgment. Creation cannot stand unchanged when God stands unveiled.',
    'Revelation 20:11 reveals the same majesty: at the Great White Throne, even heaven and earth flee from His face. If creation itself cannot stand before Him, then no sinner can stand without Christ\u2019s righteousness.',
    'God wants us to remember that the One we worship in grace today is the same One before whom all creation shakes. His holiness demands seriousness, sobriety, and surrender.',
    ('hr', ''),
    ('h3', 'Sinai Trembled'),
    'Exodus 19:16\u201318 shows Mount Sinai shaking violently when the Lord descended. \u201cThe whole mount quaked greatly.\u201d Israel learned that day that God is not casual or common. The same God whose presence shook Sinai is the One Nahum says melts mountains. We do not trifle with Him \u2014 we trust Him, fear Him, and obey Him.',
    ('hr', ''),
    ('h3', 'Saul of Tarsus Fell Down'),
    'When Christ appeared to Saul on the Damascus Road, \u201che fell to the earth\u201d (Acts 9:4). Though Saul was powerful, educated, and feared \u2014 he crumbled in the presence of Christ\u2019s glory. No man remains standing when God reveals Himself.',
    '<strong>If mountains quake and apostles fall before Him, then we should live with:</strong> Humble reverence, obedient hearts, gratitude for grace, and awareness of eternity. The God who shakes the earth in judgment is the same God who steadies the believer in mercy. Walk in holy fear, grateful that through Christ you can stand before the One before whom heaven and earth flee.',
])))

# Dec 11
entries.append(("2025-12-11T06:00:00", "Just in From Moldova \u2013 December 11, 2025", wp([
    '<em>\u201cBut let it be the hidden man of the heart, in that which is not corruptible\u2026\u201d</em> \u2014 <strong>1 Peter 3:4</strong>',
    '<em>\u201cBehold, thou desirest truth in the inward parts\u2026\u201d</em> \u2014 <strong>Psalm 51:6</strong>',
    '<strong>God Values What Man Cannot See.</strong> Both passages lift our eyes away from outward appearances and toward the heart, the place where God does His deepest work.',
    'People measure the visible \u2014 talent, beauty, presentation, and performance. But God measures the hidden man \u2014 the unseen character, the inward truth, the motives, the sincerity, the purity that only He can see.',
    'Before God uses a life publicly, He shapes a heart privately. Before God blesses a ministry visibly, He sanctifies motives invisibly. True spirituality is inward first, outward second.',
    ('hr', ''),
    ('h3', 'David Anointed in Secret (1 Samuel 16:6\u20137)'),
    'When Samuel saw Eliab\u2019s outward strength, he assumed he was the chosen king. God corrected him: \u201cThe LORD looketh on the heart.\u201d David was chosen not because of his appearance or stature, but because God saw truth and integrity inside him (Psalm 78:72). What man overlooked, God saw \u2014 the hidden man.',
    ('hr', ''),
    ('h3', 'Mary of Bethany (Luke 10:38\u201342)'),
    'Martha\u2019s service was visible; Mary\u2019s devotion was quiet, inward, and easily missed. Yet Jesus said: \u201cMary hath chosen that good part.\u201d Mary\u2019s heart \u2014 humble, teachable, quiet, and pure \u2014 reflected exactly what Peter described as \u201cthe hidden man of the heart.\u201d Her inward sincerity mattered more to Jesus than outward activity.',
    '<strong>Cultivate what God sees.</strong> God wants: Truth in the inner man. Purity before performance. Character before calling. Sincerity before service. The Christian life is not lived from the outside in, but from the inside out. When the inward is right, the outward will shine with grace, humility, and godliness.',
])))

# Dec 12
entries.append(("2025-12-12T06:00:00", "Just in From Moldova \u2013 December 12, 2025", wp([
    '<em>\u201cAnd hired counsellors against them, to frustrate their purpose, all the days of Cyrus king of Persia, even until the reign of Darius king of Persia.\u201d</em> \u2014 <strong>Ezra 4:5</strong>',
    '<em>\u201cNo weapon that is formed against thee shall prosper; and every tongue that shall rise against thee in judgment thou shalt condemn\u2026\u201d</em> \u2014 <strong>Isaiah 54:17</strong>',
    'The work of God is often opposed not by open enemies alone, but by deliberate frustration. Sometimes Christians who are selfish will frustrate your purpose. Some Christians struggle with wanting to be seen, heard or in control. They can feel threatened, overlooked or jealous. That leads them to resist or undermine the work \u2014 even if it\u2019s God\u2019s work.',
    'In Ezra\u2019s day, God\u2019s people had permission to build, resources to build, and a calling to build \u2014 yet men hired counsellors to delay, discourage, and derail the work. The opposition was calculated, persistent, and legal.',
    'But Isaiah reminds us of a higher truth: <strong>frustration is not the same as failure.</strong> Weapons may be formed, tongues may accuse, and plans may be hindered \u2014 but they shall not prosper. God allows resistance not to cancel His purpose, but to confirm that the work is truly His.',
    ('hr', ''),
    ('h3', 'Joseph in Egypt (Genesis 37\u201350)'),
    'Joseph\u2019s God-given purpose was frustrated repeatedly \u2014 betrayed by his brothers, falsely accused by Potiphar\u2019s wife, forgotten in prison. Yet every attempt to bury his calling only positioned him closer to God\u2019s fulfillment. What men meant for evil, God meant for good (Genesis 50:20). The weapons formed against Joseph did not prosper; they became stepping stones to the throne.',
    ('hr', ''),
    ('h3', 'Paul the Apostle (Acts 16:22\u201326)'),
    'Paul was beaten and imprisoned in Philippi for preaching Christ. Men frustrated his mission by chains and walls \u2014 but at midnight, God shook the prison. The gospel advanced, a jailer was saved, and a church was born. Men tried to silence the message, but God turned the prison into a pulpit.',
    '<strong>When men frustrate your purpose, remember:</strong> They can delay the work, but they cannot defeat the will of God. Weapons may form \u2014 but they will not prosper. Tongues may accuse \u2014 but God will justify. What God has ordained, no hired counsellor can cancel.',
])))

# Dec 13
entries.append(("2025-12-13T06:00:00", "Just in From Moldova \u2013 December 13, 2025", wp([
    '<em>\u201cBut he that hateth his brother is in darkness, and walketh in darkness, and knoweth not whither he goeth, because that darkness hath blinded his eyes.\u201d</em> \u2014 <strong>1 John 2:11</strong>',
    '<em>\u201cThe way of the wicked is as darkness: they know not at what they stumble.\u201d</em> \u2014 <strong>Proverbs 4:19</strong>',
    'Both passages reveal a sobering truth: <strong>spiritual darkness produces spiritual blindness.</strong> In 1 John, hatred toward a brother is not merely a relational failure \u2014 it is evidence of a heart walking in darkness. In Proverbs, wickedness is pictured as a path so dark that a man cannot even identify what causes his fall.',
    'When love is absent, light is absent; and when light is absent, direction is lost. Darkness deceives. A person walking in it may feel confident, justified, or even religious, yet remains unaware of the very things causing repeated failure. Only the light of God\u2019s truth and love exposes the path and restores clarity.',
    ('hr', ''),
    ('h3', 'Cain (Genesis 4:3\u20138)'),
    'Cain\u2019s hatred toward his brother Abel blinded him. Though God warned him \u2014 \u201csin lieth at the door\u201d \u2014 Cain walked on in darkness. He did not see that his anger would lead to murder. Darkness hid the consequence until the moment he stumbled into irreversible sin. Hatred darkened his understanding and severed his fellowship with God.',
    ('hr', ''),
    ('h3', 'Judas Iscariot (John 13:21\u201330)'),
    'Judas walked with Christ, heard His teaching, and witnessed His miracles \u2014 yet his heart was darkened by covetousness and bitterness. When he left the upper room to betray the Lord, Scripture notes, \u201cand it was night.\u201d Judas did not know at what he stumbled until it was too late. Darkness blinded him, even while standing near the Light of the world.',
    '<strong>Darkness is not merely the absence of knowledge \u2014 it is the absence of love and truth ruling the heart.</strong> When believers harbor hatred, bitterness, or secret sin, the path grows dark and stumbling becomes inevitable. Walking in love is walking in light; and walking in light restores sight, direction, and fellowship with God.',
])))

# Dec 14
entries.append(("2025-12-14T06:00:00", "Just in From Moldova \u2013 December 14, 2025", wp([
    '<em>\u201cAnd every man that hath this hope in him purifieth himself, even as he is pure.\u201d</em> \u2014 <strong>1 John 3:3</strong>',
    '<em>\u201cHaving therefore these promises, dearly beloved, let us cleanse ourselves from all filthiness of the flesh and spirit, perfecting holiness in the fear of God.\u201d</em> \u2014 <strong>2 Corinthians 7:1</strong>',
    '<strong>Biblical hope is not passive waiting \u2014 it is active cleansing.</strong> John teaches that when a believer truly lives in the hope of Christ\u2019s return, that hope works inwardly, producing purity. Paul echoes this truth by reminding us that God\u2019s promises demand a response: separation from sin and growth in holiness.',
    'Hope looks forward, but holiness works now. The expectation of seeing Christ does not lead to carelessness; it leads to carefulness. When eternity grips the heart, sin loses its appeal, and holiness becomes the believer\u2019s pursuit.',
    ('hr', ''),
    ('h3', 'Joseph in Egypt (Genesis 39:7\u201312)'),
    'Joseph resisted temptation because he lived with a God-conscious heart: \u201cHow then can I do this great wickedness, and sin against God?\u201d His hope was not in circumstance but in God\u2019s presence and promise. That hope produced purity in a moment of great pressure.',
    ('hr', ''),
    ('h3', 'The Wise Virgins (Matthew 25:1\u201310)'),
    'The wise virgins lived in expectation of the bridegroom\u2019s arrival. Their readiness \u2014 trimmed lamps and prepared oil \u2014 pictured hearts kept clean and watchful. Hope made them prepared; purity made them ready.',
    '<strong>Those who truly hope in Christ do not wait idly \u2014 they wash, watch, and walk carefully.</strong> God\u2019s promises purify His people, and the certainty of seeing Christ calls us to live clean until He comes.',
])))

# Dec 15
entries.append(("2025-12-15T06:00:00", "Just in From Moldova \u2013 December 15, 2025", wp([
    '<em>\u201cAnd now for a little space grace hath been shewed from the LORD our God, to leave us a remnant to escape, and to give us a nail in his holy place, that our God may lighten our eyes, and give us a little reviving in our bondage.\u201d</em> \u2014 <strong>Ezra 9:8</strong>',
    '<em>\u201cTo bring back his soul from the pit, to be enlightened with the light of the living.\u201d</em> \u2014 <strong>Job 33:30</strong>',
    'Ezra speaks of \u201ca little space grace\u201d \u2014 a brief but merciful opening from God where hope is restored, vision is renewed, and strength is given to rise again. Job declares God\u2019s purpose in that grace: to bring the soul back from the pit and to enlighten it with living light.',
    'Grace is not merely pardon; it is revival in bondage, light in darkness, and life where death seemed certain. God gives space \u2014 not to excuse sin \u2014 but to rescue, restore, and redirect the heart.',
    ('hr', ''),
    ('h3', 'Manasseh: Light After the Pit (2 Chronicles 33:11\u201313)'),
    'King Manasseh sank into deep rebellion and idolatry and was carried away in chains to Babylon \u2014 a pit of his own making. Yet God granted him a little space of grace. In affliction, Manasseh humbled himself and prayed, and the LORD brought him back. God enlightened his eyes, restored him to Jerusalem, and Manasseh knew that the LORD was God. This is Job 33:30 in living color \u2014 a soul brought back from the pit and enlightened with living light.',
    ('hr', ''),
    ('h3', 'The Prodigal Son: Reviving in Bondage (Luke 15:17\u201324)'),
    'The prodigal descended into famine, filth, and servitude \u2014 bondage far from the father\u2019s house. Yet he was given space to come to himself. When he returned, the father ran to meet him, restored him, and declared, \u201cThis my son was dead, and is alive again.\u201d Grace did not minimize his failure; it revived him, clothed him, and brought him home.',
    '<strong>When God gives you a little space, do not waste it.</strong> That opening is mercy calling you upward \u2014 from the pit to the light, from bondage to reviving. Grace always has a purpose: to restore sight, renew life, and set the heart firmly again in God\u2019s holy place.',
])))

# Dec 16
entries.append(("2025-12-16T06:00:00", "Just in From Moldova \u2013 December 16, 2025", wp([
    '<em>\u201c\u2026that ye should earnestly contend for the faith which was once delivered unto the saints.\u201d</em> \u2014 <strong>Jude 3</strong>',
    '<em>\u201cNeither is there salvation in any other: for there is none other name under heaven given among men, whereby we must be saved.\u201d</em> \u2014 <strong>Acts 4:12</strong>',
    'Jude calls believers to earnestly contend \u2014 to stand firmly, lovingly, and courageously for the unchanging faith. Acts 4:12 defines the heart of that faith: salvation in Christ alone. To contend is not to quarrel, but to guard the gospel, refusing to dilute, replace, or broaden what God has clearly declared. In every generation, the pressure is the same \u2014 to soften exclusivity for acceptance. God calls His people to faithfulness, not popularity.',
    ('hr', ''),
    ('h3', 'Elijah on Mount Carmel (1 Kings 18:21\u201339)'),
    'Elijah stood alone against compromise and cried, \u201cHow long halt ye between two opinions?\u201d He contended for the truth that the LORD alone is God. When fire fell from heaven, it proved there was no alternative power. Just as Elijah rejected divided worship, believers today must reject divided salvation \u2014 one God, one way.',
    ('hr', ''),
    ('h3', 'Peter Before the Sanhedrin (Acts 4:8\u201312)'),
    'Surrounded by religious leaders, Peter boldly declared that salvation is found only in Jesus Christ. He did not adjust the message to avoid persecution. He contended for the faith by proclaiming the exclusive name of Christ, even when it cost him.',
    '<strong>To contend for the faith is to cling to Christ alone, defend His gospel without apology, and trust God with the results.</strong> Truth guarded is truth preserved.',
])))

# Dec 17
entries.append(("2025-12-17T06:00:00", "Just in From Moldova \u2013 December 17, 2025", wp([
    '<em>\u201cWho art thou, O great mountain? before Zerubbabel thou shalt become a plain: and he shall bring forth the headstone thereof with shoutings, crying, Grace, grace unto it.\u201d</em> \u2014 <strong>Zechariah 4:7</strong>',
    '<em>\u201cTo the praise of the glory of his grace, wherein he hath made us accepted in the beloved.\u201d</em> \u2014 <strong>Ephesians 1:6</strong>',
    'Every servant of God faces a mountain \u2014 an obstacle too large for human strength, too immovable for human wisdom. Zerubbabel stood before such a mountain, not with an army or resources, but with a promise: God\u2019s work would be finished by grace, not might (Zech. 4:6). The mountain did not move because Zerubbabel was strong. It became a plain because grace was sufficient.',
    'That same grace now speaks over the believer. In Christ, we do not labor to be accepted \u2014 we labor because we are accepted. God has already declared our standing: \u201caccepted in the beloved.\u201d <strong>Grace not only removes obstacles; it establishes identity.</strong> What began with \u201cGrace, grace\u201d in Zechariah ends with \u201cthe praise of the glory of his grace\u201d in Ephesians. Grace finishes what it starts.',
    ('hr', ''),
    ('h3', 'David and Goliath (1 Samuel 17)'),
    'David did not conquer Goliath by armor or experience. He stepped forward in dependence upon God, declaring, \u201cthe battle is the LORD\u2019S\u201d (1 Sam. 17:47). The mountain fell \u2014 not because David was mighty, but because God\u2019s grace made the impossible possible.',
    ('hr', ''),
    ('h3', 'The Prodigal Son (Luke 15:20\u201324)'),
    'The prodigal returned rehearsing a speech of unworthiness. But the father interrupted him with acceptance before explanation. Robe, ring, and feast came before the apology was finished. This is grace: accepted in the beloved, not restored by merit.',
    '<strong>Grace removes the mountain, completes the work, and secures the standing.</strong> The Christian life begins, continues, and ends \u2014 not with human effort \u2014 but with grace, grace.',
])))

# Dec 18
entries.append(("2025-12-18T06:00:00", "Just in From Moldova \u2013 December 18, 2025", wp([
    '<em>\u201cRejoice greatly, O daughter of Zion; shout, O daughter of Jerusalem: behold, thy King cometh unto thee: he is just, and having salvation; lowly, and riding upon an ass, and upon a colt the foal of an ass.\u201d</em> \u2014 <strong>Zechariah 9:9</strong>',
    '<em>\u201cAnd she shall bring forth a son, and thou shalt call his name JESUS: for he shall save his people from their sins.\u201d</em> \u2014 <strong>Matthew 1:21</strong>',
    'Zechariah 9:9 reveals a King unlike any other \u2014 just, saving, and lowly. He does not arrive with banners of war, but with the posture of meekness. Matthew 1:21 gives the reason for that humility: His mission was salvation, not domination. The lowly entrance of Christ matches the lowly purpose of His coming \u2014 to save sinners, not to exalt sinners.',
    'The world expects salvation through power, force, and self-assertion. God brings salvation through humility, obedience, and grace. The King comes low so that fallen men might be lifted high.',
    ('hr', ''),
    ('h3', 'David before Goliath (1 Samuel 17)'),
    'David did not come in Saul\u2019s armor or with a warrior\u2019s display. He came as a shepherd boy, armed only with faith in God. Israel\u2019s victory did not come through size or spectacle, but through humble dependence upon the Lord. Just as David\u2019s lowly appearance preceded a great deliverance, Christ\u2019s humble coming preceded eternal salvation.',
    ('hr', ''),
    ('h3', 'Jesus Washing the Disciples\u2019 Feet (John 13:3\u20135)'),
    'The One who knew He had come from God and was returning to God laid aside His garments and washed the feet of His followers. This act pictured the heart of Matthew 1:21 \u2014 a Savior who stoops to cleanse. The same Jesus who saves from sin first humbled Himself to serve.',
    '<strong>Salvation does not come by human strength or religious display, but by trusting the lowly Savior.</strong> Christ still comes gently \u2014 into hearts that will receive Him. If the King came low to save us, we must walk low to follow Him. \u201cGod resisteth the proud, but giveth grace unto the humble.\u201d (James 4:6).',
])))

# Dec 19
entries.append(("2025-12-19T06:00:00", "Just in From Moldova \u2013 December 19, 2025", wp([
    '<em>\u201cAnd I will feed the flock of slaughter, even you, O poor of the flock. And I took unto me two staves; the one I called Beauty, and the other I called Bands; and I fed the flock.\u201d</em> \u2014 <strong>Zechariah 11:7</strong>',
    '<em>\u201cAnd other sheep I have, which are not of this fold: them also I must bring, and they shall hear my voice; and there shall be one fold, and one shepherd.\u201d</em> \u2014 <strong>John 10:16</strong>',
    'In Zechariah 11:7, the Lord identifies Himself as the true Shepherd who feeds the flock \u2014 especially \u201cthe poor of the flock.\u201d The two staves reveal His shepherding heart: <strong>Beauty</strong> (grace, favor, covenant kindness) and <strong>Bands</strong> (unity, binding together). Even when the flock is vulnerable, the Shepherd does not abandon them.',
    'In John 10:16, Jesus declares the fulfillment of that shepherd promise. He will gather \u201cother sheep\u201d (Gentiles) so that all who hear His voice become one flock under one Shepherd. Unity is not organizational \u2014 it is spiritual, created by Christ\u2019s voice and sustained by His care.',
    ('hr', ''),
    ('h3', 'Joseph Gathering Jacob\u2019s Family (Genesis 45\u201347)'),
    'Though scattered by famine and family conflict, God used Joseph to feed and preserve the house of Israel in Egypt. The same hand that provided bread also bound the family together again. The shepherding God fed the needy and united a broken flock \u2014 Beauty and Bands in action.',
    ('hr', ''),
    ('h3', 'The Conversion of Cornelius (Acts 10\u201311)'),
    'Peter is sent to a Gentile household, and the Holy Ghost falls upon them as upon the Jews. God makes it clear: these \u201cother sheep\u201d belong to the same Shepherd. What God had joined, no man could divide. The flock became one \u2014 not by tradition, but by the Shepherd\u2019s voice.',
    '<strong>The mark of Christ\u2019s shepherding is not merely provision, but unity under His voice.</strong> When we submit to the Shepherd, He feeds us with grace and binds us together in truth \u2014 one flock, one Shepherd.',
])))

# Dec 20
entries.append(("2025-12-20T06:00:00", "Just in From Moldova \u2013 December 20, 2025", wp([
    '<em>\u201cAnd one shall say unto him, What are these wounds in thine hands? Then he shall answer, Those with which I was wounded in the house of my friends.\u201d</em> \u2014 <strong>Zechariah 13:6</strong>',
    '<em>\u201cFaithful are the wounds of a friend; but the kisses of an enemy are deceitful.\u201d</em> \u2014 <strong>Proverbs 27:6</strong>',
    'God teaches that not all wounds are evil, and not all kindness is love. Some wounds are faithful, and some embraces are fatal. Zechariah speaks of wounds received in the house of friends \u2014 injuries that come not from enemies, but from those close enough to correct, confront, and care.',
    'Faithful wounds expose error, stop deception, and rescue the soul. Deceitful kisses, however, preserve peace at the price of truth. They soothe pride but leave sin untouched. <strong>God values truth spoken in love more than comfort that leads to destruction.</strong>',
    ('hr', ''),
    ('h3', 'Nathan and David (2 Samuel 12:1\u20137)'),
    'Nathan came to David not with flattery, but with truth. His words pierced the king\u2019s heart: \u201cThou art the man.\u201d That confrontation wounded David\u2019s pride, but healed his soul. Had Nathan remained silent, David would have continued in sin. The wound was faithful \u2014 and restoration followed.',
    ('hr', ''),
    ('h3', 'Paul and Peter (Galatians 2:11\u201314)'),
    'Paul withstood Peter \u201cto the face\u201d because Peter\u2019s conduct endangered the truth of the gospel. This was no act of hostility, but of holy love. The correction protected the church and preserved doctrine. A faithful wound saved many from confusion.',
    '<strong>God often uses loving correction to leave marks that remind us of His care.</strong> When truth wounds us, we must ask: Is this an enemy attacking \u2014 or a friend rescuing? The wounds God allows from faithful voices are instruments of grace, guiding us back to righteousness. Faithful wounds heal deeply; deceitful kisses destroy quietly.',
])))

# Dec 21
entries.append(("2025-12-21T06:00:00", "Just in From Moldova \u2013 December 21, 2025", wp([
    '<em>\u201cYe looked for much, and, lo, it came to little; and when ye brought it home, I did blow upon it. Why? saith the LORD of hosts. Because of mine house that is waste, and ye run every man unto his own house.\u201d</em> \u2014 <strong>Haggai 1:9</strong>',
    '<em>\u201cThe grass withereth, the flower fadeth: because the spirit of the LORD bloweth upon it: surely the people is grass.\u201d</em> \u2014 <strong>Isaiah 40:7</strong>',
    'God reminds His people that <strong>anything pursued apart from Him is subject to His breath.</strong> In Haggai, the people were busy, productive, and prosperous in appearance \u2014 yet God blew upon their gains, and it came to little. In Isaiah, human strength, beauty, and achievement are likened to grass \u2014 impressive for a moment, but unable to stand when the breath of the LORD passes over it.',
    'The lesson is sobering and gracious: what God does not sustain, God will not allow to stand. When priorities drift from God\u2019s glory to self-interest, even honest labor loses its blessing. But when God\u2019s will is first, His breath gives life instead of loss.',
    ('hr', ''),
    ('h3', 'The Tower of Babel (Genesis 11:1\u20139)'),
    'Men united their skills, strength, and vision to build a tower reaching heaven \u2014 without God. Their project looked unstoppable, but with a word, God confounded their language. What seemed permanent fell apart instantly. God blew upon human ambition, and it scattered.',
    ('hr', ''),
    ('h3', 'The Rich Fool (Luke 12:16\u201321)'),
    'The man\u2019s fields prospered, and his barns overflowed. He planned a future of ease \u2014 yet God said, \u201cThou fool, this night thy soul shall be required of thee.\u201d In one breath, all he trusted vanished. His success stood only until God spoke.',
    '<strong>If God\u2019s breath is against a thing, it will fade. If God\u2019s breath is upon a thing, it will flourish.</strong> The safest place for any life, labor, or ministry is under the sustaining breath of God.',
])))

# Dec 22-31 and Jan 1-4 continue in next part
print(f"Part 1: {len(entries)} entries ready")

# Post them
for i, (date, title, content) in enumerate(entries):
    pid, link = post_entry(date, title, content)
    print(f"  [{i+1}/{len(entries)}] {title} -> ID={pid}")
    time.sleep(0.5)
