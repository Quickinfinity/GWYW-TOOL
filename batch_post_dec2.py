#!/usr/bin/env python3
"""Batch post Daily Manna entries: Dec 22-31, 2025 + Jan 1, 3, 4, 2026"""

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
    return "\n\n".join(blocks)

entries = []

# Dec 22
entries.append(("2025-12-22T06:00:00", "Just in From Moldova \u2013 December 22, 2025", wp([
    '<em>\u201cSet a watch, O LORD, before my mouth; keep the door of my lips.\u201d</em> \u2014 <strong>Psalm 141:3</strong>',
    '<em>\u201cIf any man among you seem to be religious, and bridleth not his tongue, but deceiveth his own heart, this man\u2019s religion is vain.\u201d</em> \u2014 <strong>James 1:26</strong>',
    'The tongue is the gatekeeper of the heart. David did not trust his own discipline to control it \u2014 he prayed for God to set the guard. James warns that outward religion collapses when the tongue runs unrestrained. Words can either testify to a surrendered heart or expose a deceived one. True spirituality is revealed not by how loudly we worship, but by how carefully we speak.',
    ('hr', ''),
    ('h3', 'Moses at the Rock (Numbers 20:7\u201312)'),
    'Moses obeyed God outwardly, but his words betrayed a frustrated heart. In anger, he spoke rashly and struck the rock. The miracle still happened, but Moses lost the privilege of entering Canaan. This shows that God weighs words as seriously as actions \u2014 one unguarded moment of speech can cost long-term blessing.',
    ('hr', ''),
    ('h3', 'Peter\u2019s Denial (Matthew 26:69\u201375)'),
    'Peter loved Christ sincerely, yet when pressure came, his tongue spoke fear instead of faith. Three denials flowed from an unguarded mouth, followed by bitter tears. Later, restored by Christ, Peter learned restraint and boldness governed by the Spirit. The same tongue that denied the Lord was later used to preach at Pentecost \u2014 once surrendered to God\u2019s control.',
    '<strong>Before words ever reach others, they pass through the heart.</strong> Pray daily for a guarded mouth, because uncontrolled speech doesn\u2019t just harm others \u2014 it empties our testimony of power. A watched mouth reflects a worshipful heart.',
])))

# Dec 23
entries.append(("2025-12-23T06:00:00", "Just in From Moldova \u2013 December 23, 2025", wp([
    '<em>\u201c\u2026but their nobles put not their necks to the work of their Lord.\u201d</em> \u2014 <strong>Nehemiah 3:5</strong>',
    '<em>\u201cTake my yoke upon you, and learn of me; for I am meek and lowly in heart: and ye shall find rest unto your souls.\u201d</em> \u2014 <strong>Matthew 11:29</strong>',
    'Nehemiah records a striking contrast in the rebuilding of Jerusalem\u2019s wall. Many labored willingly, yet the nobles of the Tekoites refused to bend their necks \u2014 they would not submit to the work God had given. Pride kept them from partnership, and status kept them from service.',
    'In contrast, the Lord Jesus calls us not to resist His yoke, but to take it. His yoke is not crushing but calming; not heavy with pride, but light with humility. <strong>Refusing God\u2019s yoke leads to wasted opportunity; receiving Christ\u2019s yoke leads to rest for the soul.</strong>',
    ('hr', ''),
    ('h3', 'Rehoboam\u2019s Stiff Neck (1 Kings 12:6\u201316)'),
    'When Rehoboam rejected the counsel to serve the people with gentleness, he chose a heavier yoke of pride. His refusal to humble himself split the kingdom. Like the nobles in Nehemiah\u2019s day, he would not bow his neck \u2014 and the work of unity was lost. Pride resists the yoke; humility preserves the work of God.',
    ('hr', ''),
    ('h3', 'John the Baptist\u2019s Willing Decrease (John 3:29\u201330)'),
    'John the Baptist gladly stepped aside, saying, \u201cHe must increase, but I must decrease.\u201d He embraced Christ\u2019s yoke by yielding prominence and submitting to God\u2019s purpose. In doing so, John found joy, not loss. The meek yoke of Christ brings peace where self-rule only brings strain.',
    '<strong>God\u2019s work advances through yielded hearts.</strong> The question is not whether there is a yoke \u2014 but whose yoke we will bear. To refuse the Lord\u2019s yoke is to miss His work; to receive it is to find rest while serving.',
])))

# Dec 24
entries.append(("2025-12-24T06:00:00", "Just in From Moldova \u2013 December 24, 2025", wp([
    '<em>\u201cTherefore the Lord himself shall give you a sign; Behold, a virgin shall conceive, and bear a son, and shall call his name Immanuel.\u201d</em> \u2014 <strong>Isaiah 7:14</strong>',
    '<em>\u201cAnd she brought forth a man child, who was to rule all nations with a rod of iron: and her child was caught up unto God, and to his throne.\u201d</em> \u2014 <strong>Revelation 12:5</strong>',
    'Isaiah declares the miracle of the promised Son \u2014 Immanuel, God with us. Revelation reveals the destiny of that same Son \u2014 ruler of all nations, preserved from the enemy and exalted to God\u2019s throne. <strong>What God promises in prophecy, He protects in history and fulfills in glory.</strong> The child born in humility is the King crowned in heaven. Satan may oppose, but he cannot overturn God\u2019s redemptive plan.',
    ('hr', ''),
    ('h3', 'Isaac, the Child of Promise (Genesis 21:1\u20137)'),
    'Isaac was born exactly as God promised, despite impossibility and delay. Threats arose later (Genesis 22), yet God preserved the promised son. Isaac\u2019s life illustrates that when God gives a promise tied to His covenant, He also guards its fulfillment \u2014 just as with Christ, the greater promised Son.',
    ('hr', ''),
    ('h3', 'Christ Preserved and Exalted (Matthew 2:13\u201315; Acts 2:32\u201336)'),
    'Herod sought to destroy the Child, but God protected Him, just as Revelation foretells. Later, though men crucified Him, God raised Him and exalted Him. The dragon could not devour the Child; the grave could not hold the King.',
    '<strong>God not only keeps His promise \u2014 He completes it in victory.</strong> The same God who promised Christ, preserved Christ, and exalted Christ is faithful to His Word today. What He begins, He will finish \u2014 no matter the opposition.',
])))

# Dec 25
entries.append(("2025-12-25T06:00:00", "Just in From Moldova \u2013 December 25, 2025", wp([
    '<em>\u201cFor unto you is born this day in the city of David a Saviour, which is Christ the Lord.\u201d</em> \u2014 <strong>Luke 2:11</strong>',
    '<em>\u201cThe first man is of the earth, earthy: the second man is the Lord from heaven.\u201d</em> \u2014 <strong>1 Corinthians 15:47</strong>',
    'Luke announces a birth on earth, while Paul explains a nature from heaven. Jesus did not merely arrive as another man \u2014 He came as the Second Man, sent from heaven to do what the first man, Adam, could not do.',
    'Adam brought sin and death to the earth; Christ brought righteousness and life from heaven. The manger in Bethlehem reveals God stepping into human history, but 1 Corinthians 15:47 reveals why \u2014 salvation could not rise from earth; it had to come down from heaven. What was ruined by the first man could only be restored by the Man from heaven.',
    ('hr', ''),
    ('h3', 'The First Adam vs. The Promised Seed'),
    '<strong>Genesis 3:6</strong> \u2014 Adam\u2019s fall brought death. <strong>Genesis 3:15</strong> \u2014 God promised a coming Deliverer. Adam was formed from the dust of the ground, but God promised One who would come by divine intervention, not human effort. Luke 2:11 is the fulfillment of that promise \u2014 the heavenly solution to an earthly failure. Earth could not fix what earth broke.',
    ('hr', ''),
    ('h3', 'The Empty Tomb'),
    '<strong>Romans 5:19</strong> \u2014 \u201cBy the obedience of one shall many be made righteous.\u201d <strong>1 Corinthians 15:22</strong> \u2014 \u201cFor as in Adam all die, even so in Christ shall all be made alive.\u201d The Second Man proved His heavenly origin not only by His birth, but by His resurrection. The stone rolled away declared that heaven\u2019s Man had conquered earth\u2019s curse.',
    '<strong>You are either identified with the first man, Adam, or the second Man, Christ.</strong> Luke says He was born for you. Paul says He came from heaven. Salvation is not self-improvement \u2014 it is a new Man, given by God. \u201cThe second man is the Lord from heaven.\u201d',
])))

# Dec 26
entries.append(("2025-12-26T06:00:00", "Just in From Moldova \u2013 December 26, 2025", wp([
    '<em>\u201cThese shall make war with the Lamb, and the Lamb shall overcome them: for he is Lord of lords, and King of kings: and they that are with him are called, and chosen, and faithful.\u201d</em> \u2014 <strong>Revelation 17:14</strong>',
    '<em>\u201cWhich in his times he shall shew, who is the blessed and only Potentate, the King of kings, and Lord of lords.\u201d</em> \u2014 <strong>1 Timothy 6:15</strong>',
    'Both passages lift our eyes above earthly power and passing authority to the unchallenged rule of Christ. Kings may rise, systems may resist Him, and the world may appear united against truth \u2014 but the outcome is already settled. <strong>The Lamb overcomes.</strong> He reigns not by permission, but by position. And those who stand with Him are not merely spectators; they are called, chosen, and faithful.',
    'As we approach the New Year, this devotion reminds us that faithfulness is never wasted, even when opposition seems strong. Christ does not borrow authority \u2014 He is authority.',
    ('hr', ''),
    ('h3', 'David and Goliath (1 Samuel 17)'),
    'Goliath stood as the champion of worldly strength, armed and confident. David appeared insignificant by comparison \u2014 yet he came \u201cin the name of the LORD of hosts\u201d (1 Sam. 17:45). The battle was decided not by size or weaponry, but by sovereignty. God\u2019s chosen servant stands secure because the Lord reigns.',
    ('hr', ''),
    ('h3', 'Christ Before Pilate (John 18:33\u201337)'),
    'Pilate questioned Jesus about His kingship, unaware that he stood before the very One who held ultimate authority. Jesus calmly declared, \u201cMy kingdom is not of this world.\u201d Though appearing bound, Christ was never dethroned. The cross did not defeat Him \u2014 it crowned Him.',
    '<strong>When the world opposes truth, remember who wins.</strong> Serve faithfully. Stand confidently. Follow the Lamb. He is still King of kings and Lord of lords \u2014 and those who are with Him will overcome.',
])))

# Dec 27
entries.append(("2025-12-27T06:00:00", "Just in From Moldova \u2013 December 27, 2025", wp([
    '<em>\u201c\u2026were porters keeping the ward at the thresholds of the gates.\u201d</em> \u2014 <strong>Nehemiah 12:25</strong>',
    '<em>\u201cMoreover it is required in stewards, that a man be found faithful.\u201d</em> \u2014 <strong>1 Corinthians 4:2</strong>',
    'In Nehemiah\u2019s day, the porters were not in the spotlight. They stood at the thresholds, carrying the burden of vigilance \u2014 guarding, watching, and remaining steady while others celebrated. Their task was not glamorous, but it was essential.',
    'The Apostle Paul reminds us that God does not first require brilliance, strength, or recognition \u2014 He requires faithfulness. To carry the burdens God assigns is to stand where He places us and hold the trust He gives us, even when the work is heavy and unseen. <strong>Faithfulness is often measured not by how loudly we serve, but by how long we endure.</strong>',
    ('hr', ''),
    ('h3', 'The Levites Bearing the Ark'),
    'When Israel traveled, the Levites carried the ark of the covenant (Numbers 4:15). The ark was heavy, holy, and dangerous if handled carelessly. They could not set it down casually or delegate the task. Their burden was sacred, and their faithfulness preserved the presence of God among the people.',
    ('hr', ''),
    ('h3', 'Simon of Cyrene'),
    'As Jesus bore the cross, the soldiers compelled Simon of Cyrene to carry it behind Him (Luke 23:26). Simon did not volunteer, nor did he preach \u2014 but for a moment, he carried a burden connected directly to redemption itself. Faithful stewardship sometimes means carrying what we did not choose, yet God uses that burden to shape lives and reveal Christ.',
    '<strong>God entrusts burdens to those He can trust with faithfulness.</strong> Whether standing at the gate, bearing the ark, or carrying a cross \u2014 the Lord honors those who quietly carry the burdens He assigns. \u201cWell done, thou good and faithful servant\u2026\u201d (Matthew 25:21).',
])))

# Dec 28
entries.append(("2025-12-28T06:00:00", "Just in From Moldova \u2013 December 28, 2025", wp([
    '<em>\u201cAnd he was clothed with a vesture dipped in blood: and his name is called The Word of God.\u201d</em> \u2014 <strong>Revelation 19:13</strong>',
    '<em>\u201cFor there are three that bear record in heaven, the Father, the Word, and the Holy Ghost: and these three are one.\u201d</em> \u2014 <strong>1 John 5:7</strong>',
    'These two verses unite heaven and earth around one glorious truth: <strong>God reveals Himself through His Word \u2014 living, eternal, and unified.</strong> In Revelation, Jesus is revealed as \u201cThe Word of God\u201d \u2014 not merely a messenger of truth, but truth embodied, marked by sacrifice and authority. In 1 John, that same Word stands eternally with the Father and the Holy Ghost, bearing record in heaven.',
    'What heaven declares in unity, earth experiences in redemption. The Word who was with God came clothed in blood so that sinners could be clothed in righteousness.',
    ('hr', ''),
    ('h3', 'The Blood on the Doorposts (Exodus 12)'),
    'When Israel was in Egypt, deliverance came not by strength, but by obedience to God\u2019s spoken word. The blood applied to the doorposts spared the household from judgment. The destroying angel did not look inside the home \u2014 he looked for the blood. God\u2019s Word, when believed and obeyed, brings life and deliverance through blood-appointed redemption.',
    ('hr', ''),
    ('h3', 'The Word Made Flesh (John 1:1\u201314)'),
    'John declares that \u201cthe Word was made flesh, and dwelt among us.\u201d The eternal Word stepped into time, spoke grace and truth, and went to the cross. At Calvary, the Word was silent before men, yet speaking loudly before heaven. The same Word that bears record in heaven bears wounds on earth \u2014 so sinners might believe and live.',
    '<strong>The Word is eternal (1 John 5:7). The Word is revealed (Revelation 19:13). The Word is redemptive.</strong> Do not treat Scripture as mere text \u2014 it is the living testimony of a triune God, written in ink, fulfilled in blood, and confirmed in heaven. The Word still speaks. The blood still saves. And heaven still bears record.',
])))

# Dec 29
entries.append(("2025-12-29T06:00:00", "Just in From Moldova \u2013 December 29, 2025", wp([
    '<em>\u201cAnd Esther said, The adversary and enemy is this wicked Haman.\u201d</em> \u2014 <strong>Esther 7:6</strong>',
    '<em>\u201cThe wrath of a king is as messengers of death: but a wise man will pacify it.\u201d</em> \u2014 <strong>Proverbs 16:14</strong>',
    'There is a solemn moment when hidden evil is brought into the light just before judgment falls. In Esther\u2019s day, Haman sat confidently at the king\u2019s table \u2014 yet his fate was already sealed. The queen\u2019s words did not create the danger; they revealed it.',
    'Proverbs reminds us that royal wrath is no small matter \u2014 it is decisive, swift, and final. Wisdom is not found in hiding sin, but in turning from it before exposure comes. <strong>Mercy precedes judgment \u2014 but judgment follows rejection.</strong>',
    ('hr', ''),
    ('h3', 'Haman (Esther 7)'),
    'Haman built gallows for Mordecai while dining with the king, unaware that God had already turned the king\u2019s heart. When Esther exposed him, wrath moved immediately. The gallows prepared for another became his own. What is hidden in pride will be revealed in judgment. God exposes the adversary before wrath is executed.',
    ('hr', ''),
    ('h3', 'Herod Agrippa I (Acts 12:21\u201323)'),
    'Herod accepted worship as a god and refused to give glory to God. No accusation followed \u2014 only exposure. Scripture says he was smitten by the angel of the Lord and died. When men exalt themselves against God, judgment does not need debate \u2014 only revelation.',
    '<strong>Before the King\u2019s wrath moves, God gives space for repentance.</strong> Wisdom does not challenge authority or resist truth \u2014 it pacifies by humility, confession, and fear of the Lord. What is not confessed today may be confronted tomorrow. \u201cBe sure your sin will find you out.\u201d (Numbers 32:23). Grace warns before wrath works.',
])))

# Dec 30
entries.append(("2025-12-30T06:00:00", "Just in From Moldova \u2013 December 30, 2025", wp([
    '<em>\u201cAnd God shall wipe away all tears from their eyes; and there shall be no more death, neither sorrow, nor crying, neither shall there be any more pain: for the former things are passed away.\u201d</em> \u2014 <strong>Revelation 21:4</strong>',
    '<em>\u201cHe will swallow up death in victory; and the Lord GOD will wipe away tears from off all faces; and the rebuke of his people shall he take away from off all the earth: for the LORD hath spoken it.\u201d</em> \u2014 <strong>Isaiah 25:8</strong>',
    'Both Isaiah and John speak with one voice across the centuries: <strong>God Himself will personally remove the cause and the evidence of sorrow.</strong> Tears are not merely dried by time or numbed by resignation \u2014 they are wiped away by the hand of God. Death is not managed, delayed, or softened; it is swallowed up in victory.',
    ('hr', ''),
    ('h3', 'Joseph in Egypt (Genesis 41\u201345)'),
    'Joseph endured betrayal, false accusation, imprisonment, and years of unanswered pain. Yet when God exalted him, Joseph testified that the Lord had caused him to forget his toil \u2014 not by erasing memory, but by overruling sorrow with purpose. When Joseph wept upon seeing his brothers restored, those tears were not of despair but of redemption.',
    ('hr', ''),
    ('h3', 'Mary at the Empty Tomb (John 20:11\u201316)'),
    'Mary stood weeping, believing death had won. But when the risen Christ spoke her name, her tears turned instantly to joy. Resurrection transformed grief in a moment. This scene previews Revelation 21:4 \u2014 when Christ stands before His redeemed people, every tear will be answered by His presence.',
    '<strong>What God promises in Isaiah, He fulfills in Revelation. What Christ proved at the tomb, He will complete in eternity.</strong> Until that day, every tear you shed is counted, every sorrow is temporary, and every pain is moving toward a divine conclusion. The Lord hath spoken it \u2014 and He will finish it.',
])))

# Dec 31
entries.append(("2025-12-31T06:00:00", "Just in From Moldova \u2013 December 31, 2025", wp([
    '<em>\u201cAnd there shall be no night there; and they need no candle, neither light of the sun; for the Lord God giveth them light: and they shall reign for ever and ever.\u201d</em> \u2014 <strong>Revelation 22:5</strong>',
    '<em>\u201cBut the path of the just is as the shining light, that shineth more and more unto the perfect day. The way of the wicked is as darkness: they know not at what they stumble.\u201d</em> \u2014 <strong>Proverbs 4:18\u201319</strong>',
    'The Word of God contrasts two paths \u2014 increasing light and deepening darkness. Proverbs teaches that the righteous do not merely enter the light; they walk in it, and that light grows brighter with every step of obedience. Revelation completes the picture: the journey that begins with dawning light ends in eternal day, where the Lord Himself is the Light.',
    'Darkness blinds, confuses, and causes stumbling. Light reveals, directs, and produces confidence. <strong>The Christian life is not instant perfection, but progressive illumination</strong> \u2014 more clarity, more holiness, more likeness to Christ \u2014 until the \u201cperfect day\u201d when night is forever gone.',
    ('hr', ''),
    ('h3', 'Israel and the Pillar of Fire'),
    'In Exodus 13:21\u201322, Israel journeyed through the wilderness by night under the pillar of fire. The light did not remove the wilderness, but it made the way visible. That same light which guided Israel confounded Egypt (Exodus 14:20). So it is with believers: God\u2019s light guides His people step by step, while the same light exposes and judges darkness.',
    ('hr', ''),
    ('h3', 'Paul on the Damascus Road'),
    'In Acts 9:3\u20136, Saul of Tarsus was struck down by a light from heaven brighter than the sun. That light first blinded him, revealing how dark his former way truly was. When his eyes were opened again, he walked a new path \u2014 one of growing light and obedience. Paul later testified in Acts 26:18 that the gospel turns men \u201cfrom darkness to light.\u201d His life became a living example of Proverbs 4:18 \u2014 growing brighter until the end.',
    '<strong>The believer\u2019s present walk is progressive light, and the believer\u2019s future home is perfect light.</strong> What begins with a single step of faith ends with no night at all \u2014 for \u201cthe Lord God giveth them light.\u201d Walk today in the light you have, and God will give more \u2014 until the day breaks and the shadows flee away.',
])))

# Jan 1, 2026
entries.append(("2026-01-01T06:00:00", "Just in From Moldova \u2013 January 1, 2026", wp([
    '<em>\u201cWisdom crieth without; she uttereth her voice in the streets.\u201d</em> \u2014 <strong>Proverbs 1:20</strong>',
    '<em>\u201cIn the last day, that great day of the feast, Jesus stood and cried, saying, If any man thirst, let him come unto me, and drink.\u201d</em> \u2014 <strong>John 7:37</strong>',
    'God\u2019s invitation is not whispered in secret corners \u2014 it is cried openly. In the streets of daily life, wisdom calls sinners to turn; in the courts of the temple, Christ calls the thirsty to come. Heaven does not hide truth from honest hearts. The tragedy is not that God is silent, but that many are too busy or proud to listen. <strong>Wisdom still cries; Christ still calls.</strong> The question is whether we will respond.',
    ('hr', ''),
    ('h3', 'Water from the Rock'),
    'When Israel thirsted in the wilderness, God commanded Moses to smite the rock, and water flowed freely for all the people (Exodus 17:1\u20136). The provision was public, abundant, and undeserved. No one had to earn it \u2014 only to come and drink. So it is with wisdom: God makes provision before the need overwhelms us, and He offers it openly to those who will trust Him.',
    ('hr', ''),
    ('h3', 'The Samaritan Woman'),
    'At Jacob\u2019s well, Jesus offered living water to a broken woman who came to draw physical water (John 4:10\u201314). She was not seeking theology, yet truth met her in an ordinary place. Christ\u2019s call satisfied a deeper thirst than she knew she had. Like the cry at the feast, His invitation was simple: come and drink.',
    '<strong>Wisdom cries in the streets. Jesus cries in the crowd.</strong> God\u2019s grace is public, personal, and present \u2014 for any who will hear and come.',
])))

# Jan 3, 2026
entries.append(("2026-01-03T06:00:00", "Just in From Moldova \u2013 January 3, 2026", wp([
    '<em>\u201cAnd GOD saw that the wickedness of man was great in the earth, and that every imagination of the thoughts of his heart was only evil continually.\u201d</em> \u2014 <strong>Genesis 6:5</strong>',
    '<em>\u201cLo, this only have I found, that God hath made man upright; but they have sought out many inventions.\u201d</em> \u2014 <strong>Ecclesiastes 7:29</strong>',
    'Genesis 6:5 exposes the tragic depth of man\u2019s fall. What God created upright, sin distorted inwardly. The issue is not merely behavior, but the heart \u2014 its imaginations, desires, and direction. Ecclesiastes 7:29 reminds us that God did not create man broken or corrupt; He made man upright. The corruption came when man chose his own \u201cinventions\u201d \u2014 paths of self-rule apart from God.',
    'Together, these verses teach a sobering truth: <strong>sin is not accidental; it is deliberate.</strong> Left to himself, man does not drift toward righteousness but toward rebellion. Only divine intervention can restore what sin has ruined.',
    ('hr', ''),
    ('h3', 'The Days of Noah (Genesis 6\u20137)'),
    'Before the Flood, society was advanced, busy, and inventive \u2014 but spiritually bankrupt. God\u2019s grief was not over technology or progress, but over hearts that had turned continually evil. Noah stands as a contrast: a man who \u201cfound grace in the eyes of the LORD\u201d (Genesis 6:8). While the world followed its own inventions, Noah walked with God. The ark itself illustrates God\u2019s remedy \u2014 not self-reform, but God-provided salvation.',
    ('hr', ''),
    ('h3', 'The Rich Young Ruler (Mark 10:17\u201322)'),
    'This young man appeared morally upright outwardly, yet when confronted with the call to follow Christ, his heart was exposed. He had \u201cmany possessions,\u201d but more accurately, his possessions had him. Though created upright, he had sought his own invention \u2014 security apart from Christ.',
    '<strong>God made man upright \u2014 but sin bent the heart inward.</strong> The answer is not better inventions, education, or morality, but new life. What was lost in Adam is restored in Christ. As David prayed, so must we: \u201cCreate in me a clean heart, O God; and renew a right spirit within me\u201d (Psalm 51:10). Grace does not improve the old heart \u2014 it gives a new one.',
])))

# Jan 4, 2026
entries.append(("2026-01-04T06:00:00", "Just in From Moldova \u2013 January 4, 2026", wp([
    '<em>\u201cBut the dove found no rest for the sole of her foot, and she returned unto him into the ark\u2026\u201d</em> \u2014 <strong>Genesis 8:9</strong>',
    '<em>\u201cThese things I have spoken unto you, that in me ye might have peace. In the world ye shall have tribulation: but be of good cheer; I have overcome the world.\u201d</em> \u2014 <strong>John 16:33</strong>',
    'The dove went out over a flooded world, searching for a place to rest \u2014 but found none. Though judgment was receding, the earth was not yet ready. So the dove returned to the ark, the only place of safety and peace.',
    'Jesus teaches the same truth to His disciples: the world is not a place of rest. Trouble is guaranteed here. Yet He offers something greater \u2014 <strong>peace in Himself</strong>, not the absence of storms, but calm in the midst of them. Until the world is fully renewed, the believer\u2019s rest is not found \u201cout there,\u201d but \u201cin Him.\u201d',
    ('hr', ''),
    ('h3', 'Israel in the Wilderness (Exodus 33:14)'),
    'God told Moses, \u201cMy presence shall go with thee, and I will give thee rest.\u201d The wilderness offered no rest \u2014 only trials, enemies, and uncertainty. But God\u2019s presence among His people became their place of rest. Like the dove returning to the ark, Israel learned that rest comes from God\u2019s presence, not from circumstances.',
    ('hr', ''),
    ('h3', 'Paul in the Storm (Acts 27)'),
    'While the ship was battered by violent winds, Paul stood in peace, confident in God\u2019s promise. Though the storm raged, his heart was anchored. The sea did not calm immediately \u2014 but the man of God was calm, because his trust was in the Lord who overcomes all storms.',
    '<strong>When you search the world for peace, you will find none.</strong> Like the dove, you will return weary \u2014 unless you return to Christ. The ark is still open. The Savior is still speaking peace. Until the final rest comes, our peace is not found in a place \u2014 but in a Person.',
])))

print(f"Part 2: {len(entries)} entries ready")

for i, (date, title, content) in enumerate(entries):
    pid, link = post_entry(date, title, content)
    print(f"  [{i+1}/{len(entries)}] {title} -> ID={pid}")
    time.sleep(0.5)
