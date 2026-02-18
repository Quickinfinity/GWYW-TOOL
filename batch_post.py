#!/usr/bin/env python3
import json, subprocess, time

WP_URL = "https://joequick.com/wp-json/wp/v2/posts"
USER = "joe.quick"
PASS = "A4eZRwAwtv1HN9gQz7pk3Yae"

entries = [
    {
        "date": "2025-10-21T08:00:00",
        "slug": "just-in-from-moldova-oct-21",
        "content": """<!-- wp:paragraph -->
<p><em>"Why is light given to a man whose way is hid, and whom God hath hedged in?"</em> — Job 3:23</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><em>"And hast not shut me up into the hand of the enemy: thou hast set my feet in a large room."</em> — Psalm 31:8</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>At times, life feels like Job 3:23 — confined, limited, and surrounded by walls we cannot move. Job looked at his hedge and thought it was a prison. But later, David looked at his boundary and called it protection — "Thou hast not shut me up… thou hast set my feet in a large room."</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The same hedge that frustrates us may, in fact, be the hand of God preserving us. Job's "hedge" was not punishment but preservation — a boundary God used to protect His servant from total destruction. When God closes a door or limits our path, it's not rejection; it's redirection.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>God's boundaries are not barriers to joy but bridges to safety. Faith learns to thank Him not only for open doors but also for closed paths that protect us from the unseen enemy.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Israel at the Red Sea (Exodus 14:13–22).</strong> Israel thought they were trapped — mountains on one side, Pharaoh behind, and the sea before them. Yet God had hedged them in for a purpose. The same God who seemed to confine them parted the waters before them. What they thought was limitation became liberation.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Paul in Prison (Philippians 1:12–14).</strong> Paul wrote, "The things which happened unto me have fallen out rather unto the furtherance of the gospel." What looked like a boundary became a blessing. His chains became the channel through which the gospel spread to Caesar's household.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>When you feel hemmed in by life's circumstances, remember — God's hedge is not meant to hinder but to hold you steady until His purpose unfolds. "The hedge that holds you today will open into the hallway of victory tomorrow."</p>
<!-- /wp:paragraph -->"""
    },
    {
        "date": "2025-10-22T08:00:00",
        "slug": "just-in-from-moldova-oct-22",
        "content": """<!-- wp:paragraph -->
<p><em>"Yea, ye overwhelm the fatherless, and ye dig a pit for your friend."</em> — Job 6:27</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><em>"Whoso diggeth a pit shall fall therein: and he that rolleth a stone, it will return upon him."</em> — Proverbs 26:27</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>When Job accused his friends of "digging a pit" for him, he meant that instead of helping him, they were using his pain to prove their point. They judged when they should have comforted. Proverbs warns that such traps turn back on the one who sets them. "Whoso diggeth a pit shall fall therein."</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The principle is clear: when you misuse truth to hurt someone, it eventually hurts you. Those who criticize, condemn, or manipulate others in their weakness will one day face the same snare they laid. God sees both the hand that helps and the heart that harms.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>True friends don't dig pits, they build bridges. Compassion lifts; criticism buries. Before we speak against another's fall, we should remember that the same pit could be waiting for us. <em>"For with what judgment ye judge, ye shall be judged"</em> (Matthew 7:2).</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Haman's Gallows (Esther 7:10).</strong> Haman built a gallows to destroy Mordecai, but in the end, he was hanged on it. His plot became his punishment. Just as Proverbs said, the stone rolled back on him. The trap we dig for others often becomes our own undoing.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Judas' Betrayal (Matthew 27:3–5).</strong> Judas dug a pit of betrayal for the Lord Jesus, selling Him for thirty pieces of silver. But guilt crushed him, and he fell into the very snare of despair he had set. What began as a selfish plot ended in self-destruction.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Job's words remind us: Be a healer, not a hurter. Those who dig pits of criticism will fall in them, but those who sow mercy will reap mercy. <em>"Blessed are the merciful: for they shall obtain mercy."</em> Matthew 5:7.</p>
<!-- /wp:paragraph -->"""
    },
    {
        "date": "2025-10-23T08:00:00",
        "slug": "just-in-from-moldova-oct-23",
        "content": """<!-- wp:paragraph -->
<p><em>"Now my days are swifter than a post: they flee away, they see no good."</em> — Job 9:25</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><em>"Whereas ye know not what shall be on the morrow. For what is your life? It is even a vapour, that appeareth for a little time, and then vanisheth away."</em> — James 4:14</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Life rushes past like a runner on the track of time. Job looked back and saw how swiftly his days had vanished—like a courier who delivers his message and is gone. James echoes the same truth: our life is but a vapor—visible for a moment, then gone. Every breath we take is a reminder that eternity is near. The wise heart learns to measure days by meaning, not by minutes, and to live not for the fleeting but for the forever.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The call of both Job and James is to live intentionally, redeeming the moments for God's glory. Time wasted cannot be reclaimed, but time surrendered to God becomes treasure laid up in heaven.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Hezekiah's Added Years (Isaiah 38:1–5):</strong> When King Hezekiah was told he would die, he wept and prayed. God graciously added fifteen years to his life. Those added days were a gift of mercy, but also a test of use. Sadly, Hezekiah wasted some of those years in pride and poor choices. His story reminds us that extra time means extra responsibility, to use every moment wisely.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>The Rich Fool (Luke 12:16–21):</strong> Jesus told of a man who built bigger barns, boasting of years ahead. But God said, "Thou fool, this night thy soul shall be required of thee." His wealth could not buy another sunrise. He prepared for tomorrow's comfort but not for eternity's call. He planned for time and forgot about eternity.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Life is a vapor: fragile, brief, and uncertain. Don't just count your days; make your days count. Live ready for eternity, because eternity could begin today. <em>"So teach us to number our days, that we may apply our hearts unto wisdom."</em> — Psalm 90:12</p>
<!-- /wp:paragraph -->"""
    },
    {
        "date": "2025-10-24T08:00:00",
        "slug": "just-in-from-moldova-oct-24",
        "content": """<!-- wp:paragraph -->
<p><em>"With him is strength and wisdom: the deceived and the deceiver are his."</em> — Job 12:16</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><em>"And lead us not into temptation, but deliver us from evil: For thine is the kingdom, and the power, and the glory, for ever. Amen."</em> — Matthew 6:13</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Both verses remind us that God reigns in supreme sovereignty. Nothing escapes His control — not even deception or temptation. Job saw that both the deceiver and the deceived are within God's domain. Jesus taught that deliverance from evil comes only through divine power. Satan may tempt, but he cannot triumph where God is trusted. The believer's security lies not in personal wisdom, but in the wisdom and strength that belong to the Lord.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>When we pray "deliver us from evil," we are acknowledging that only God can preserve us from the snares of the deceiver. When we say "Thine is the power," we confess that our victory is not earned but granted by His authority. The world is full of subtle lies, but God's sovereignty turns even Satan's schemes into steps of spiritual strengthening for those who trust Him.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Joseph in Egypt (Genesis 50:20):</strong> Joseph's brothers deceived their father and betrayed Joseph. Yet, years later, Joseph testified, "Ye thought evil against me; but God meant it unto good." God overruled deception to fulfill divine destiny. The deceived and deceivers were both under His control, proving Job's truth that wisdom and power belong to God.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Peter's Temptation (Luke 22:31–32):</strong> Jesus warned Peter that Satan desired to sift him as wheat, but said, "I have prayed for thee, that thy faith fail not." Though Peter was tempted and even deceived by his own pride, God used it to humble him and strengthen his faith. Christ's intercession delivered Peter from evil's ultimate snare, proving Matthew 6:13 in action — divine deliverance through divine power.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Every deceiver has limits. Every temptation has a leash. God's sovereignty is both shield and staff — protecting us from evil and guiding us through the shadows. Rest in the One whose wisdom cannot be deceived and whose power cannot be defeated.</p>
<!-- /wp:paragraph -->"""
    },
    {
        "date": "2025-10-25T08:00:00",
        "slug": "just-in-from-moldova-oct-25",
        "content": """<!-- wp:paragraph -->
<p><em>"Also now, behold, my witness is in heaven, and my record is on high."</em> — Job 16:19</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><em>"Ye are witnesses, and God also, how holily and justly and unblameably we behaved ourselves among you that believe."</em> — 1 Thessalonians 2:10</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Job and Paul both remind us of this vital truth: the testimony of a believer must stand clean before both heaven and earth.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Job's comfort came not from man's approval but from knowing that God Himself was his witness. Paul, too, appealed to both men and God as judges of his conduct. The righteous man doesn't live to please the crowd — he lives under the all-seeing eye of God.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Every word spoken, every motive hidden, and every action taken are recorded on high. When we live transparently before God, we will walk honorably before men. The strength of a Christian's influence is built on the integrity of a conscience kept clean before the Lord.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>A pure conscience before God produces a powerful testimony before men.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Daniel in Babylon (Daniel 6:4–5):</strong> Daniel's enemies "sought to find occasion against him," but "they could find none occasion nor fault." His integrity was so consistent that his only "fault" was faithfulness to God. Like Job, Daniel lived with heaven as his witness — proving that even in a pagan world, character that is right before God will withstand the scrutiny of men.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Paul before Felix (Acts 24:16):</strong> When standing before the Roman governor, Paul declared, "Herein do I exercise myself, to have always a conscience void of offence toward God, and toward men." Even in chains, Paul valued character over comfort. His conscience was his court of appeal — and God his eternal witness.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>In a world of appearances, God still values authenticity. The believer who lives with an open heart before heaven will walk with unblameable steps before men. When your conscience is clear with God, your conduct will shine before others.</p>
<!-- /wp:paragraph -->"""
    },
    {
        "date": "2025-10-26T08:00:00",
        "slug": "just-in-from-moldova-oct-26",
        "content": """<!-- wp:paragraph -->
<p><em>"For I know that my Redeemer liveth, and that he shall stand at the latter day upon the earth."</em> — Job 19:25</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><em>"Behold, he cometh with clouds; and every eye shall see him…"</em> — Revelation 1:7</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Job stood in the ashes of sorrow, misunderstood by men, yet anchored by truth. He didn't say "I hope," or "I think" — he declared with confidence, <em>"I know."</em></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I know He lives. I know He will stand upon this earth again. I know I will see Him.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Centuries later, Revelation confirms Job's hope. The same living Redeemer is the returning King. Suffering saints do not cling to fading dreams — they cling to a living Christ and a certain appearing. Every tear, trial, and test will soon bow before the King in glory. The faith that sustains us in sorrow is the same faith that rejoices in His soon return.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Noah (Genesis 6–8).</strong> For years Noah preached a coming judgment no one believed. Yet he built, obeyed, and waited. When the flood came, his faith was vindicated. Noah's steadfast assurance mirrors Job's — the righteous wait for God to stand and judge the earth. The world mocked, but God kept His promise. Faith stands firm even when time is long and the world is blind.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Stephen (Acts 7:55–56).</strong> As stones flew, heaven opened. Stephen saw "Jesus standing at the right hand of God." The same Redeemer Job trusted was standing in glory — risen, reigning, and ready to receive His servant. Stephen died seeing the Christ Job longed for and Revelation promises will return. The dying saint looked up and saw the living Redeemer.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The Redeemer lives — and He returns. The grave cannot end the believer's hope, nor can sorrow erase the promise of His appearing. With Job we know — with John we behold. Suffering looks up and sees grace. Faith looks forward and sees glory.</p>
<!-- /wp:paragraph -->"""
    },
    {
        "date": "2025-10-27T08:00:00",
        "slug": "just-in-from-moldova-oct-27",
        "content": """<!-- wp:paragraph -->
<p><em>"And thou sayest, How doth God know? can he judge through the dark cloud?"</em> — Job 22:13</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><em>"…for they say, The Lord seeth us not; the Lord hath forsaken the earth."</em> — Ezekiel 8:12</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Man has always attempted to hide sin under the cloak of secrecy. Job identifies the proud heart that questions God's sight, while Ezekiel exposes the rebellious soul that assumes God has turned His eyes away. Darkness may conceal our deeds from man, but never from God. The clouds cannot cover us, walls cannot hide us, and secrecy cannot protect us. God sees, God knows, and God judges righteously. The comforting truth for the godly is also the terrifying reality for the wicked—God is always present, and nothing escapes His eye. Secret sins are never secret to God.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Achan (Joshua 7).</strong> Achan secretly took the forbidden spoil from Jericho and hid it in his tent. No one saw him, no man suspected him—but God did. His hidden sin brought defeat to Israel and destruction to his own household. A covered sin always becomes a costly sin.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Ananias &amp; Sapphira (Acts 5:1–11).</strong> This couple attempted to deceive the church and the Holy Ghost by pretending to give all while secretly keeping back part of the price. They thought no one would know—but God knew. Their lie was exposed and judgment fell immediately. Hidden hypocrisy meets holy judgment.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The same God who sees the sinner in the dark also watches the saint in secret faithfulness. Let us walk in the light, not in the shadows of deceit. Instead of asking, "Can God see?" let us pray, <em>"Search me, O God"</em> (Psalm 139:23).</p>
<!-- /wp:paragraph -->"""
    },
    {
        "date": "2025-10-28T08:00:00",
        "slug": "just-in-from-moldova-oct-28",
        "content": """<!-- wp:paragraph -->
<p><em>"They are of those that rebel against the light; they know not the ways thereof, nor abide in the paths thereof."</em> — Job 24:13</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><em>"Who knowing the judgment of God… not only do the same, but have pleasure in them that do them."</em> — Romans 1:32</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>There are two kinds of darkness in Scripture—darkness of ignorance, and darkness of rebellion. Job shows us people who "rebel against the light." Paul describes those who know the truth, know the judgment of God, yet still choose sin and even encourage others in it. Sin is never merely a lack of knowledge—it is a rejection of divine light. When men resist God's light long enough, they can come to love darkness and celebrate it, calling evil good and good evil. True repentance begins by humbling before the light, not fighting it. To turn from the light is to walk toward judgment. To bow to the light is to walk in life, truth, and blessing.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Pharaoh (Exodus 5–14).</strong> Pharaoh knew God's power. He saw the plagues, heard God's demands, and felt God's hand. Yet he hardened his heart again and again. He rebelled against the light given him, and in the end, he plunged his nation into ruin and lost his firstborn heir. Light rejected became judgment received.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Judas Iscariot (John 13; Acts 1).</strong> Judas walked with the Light of the world, sat at the table with Him, heard God's truth daily, and watched miracles. Yet he chose betrayal, greed, and darkness. Christ warned him, graciously appealed to him, and even washed his feet, but Judas still rebelled against the light and went to "his own place." Rejecting the light always leads to ruin. Receiving the light leads to life, peace, and blessing.</p>
<!-- /wp:paragraph -->"""
    },
    {
        "date": "2025-10-29T08:00:00",
        "slug": "just-in-from-moldova-oct-29",
        "content": """<!-- wp:paragraph -->
<p><em>"When the ear heard me, then it blessed me; and when the eye saw me, it gave witness to me."</em> — Job 29:11</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><em>"When the righteous are in authority, the people rejoice: but when the wicked beareth rule, the people mourn."</em> — Proverbs 29:2</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Job remembers a time when his life and leadership brought blessing to others. He lived uprightly, feared God, cared for the needy, defended the weak, and spoke truth in love. Because of that, those who heard him blessed him and those who saw him bore witness that he was genuine.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Proverbs echoes the same truth—righteous leadership brings joy; wicked rule brings sorrow. A life lived in the fear of God lifts others, but a selfish or sinful life burdens them. True godliness is never silent or hidden—it bears fruit that others can see (Matt 5:16). When God's people walk in integrity, families are strengthened, churches rejoice, and communities see the testimony of Christ.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>A righteous life does not shine for personal praise, but God causes others to testify when a believer walks uprightly. Righteousness blesses, while sin oppresses.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Joseph (Genesis 41–45).</strong> When Joseph ruled Egypt with wisdom and humility, the nation prospered and lives were preserved. Pharaoh and the people saw his character (Gen 41:38–40). The land rejoiced under righteous leadership—a suffering world found relief through a godly man. Just as Job, Joseph's integrity brought blessing and testimony from others.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Dorcas / Tabitha (Acts 9:36–42).</strong> Dorcas served with good works and compassion. When she died, the widows stood weeping and showed the garments she had made, bearing witness to her love. Her life blessed those who "heard" and "saw" her deeds. God honored her testimony by raising her and turning many to the Lord. Her righteousness caused people to rejoice; her loss brought mourning—just as Proverbs teaches.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Live so that when people hear you, they bless God, and when they see you, they can testify that Christ lives in you. Leadership isn't position—it's service, integrity, and visible faithfulness. Let us labor to be the kind of people whose presence brings rejoicing—not mourning.</p>
<!-- /wp:paragraph -->"""
    },
    {
        "date": "2025-10-30T08:00:00",
        "slug": "just-in-from-moldova-oct-30",
        "content": """<!-- wp:paragraph -->
<p><em>"But there is a spirit in man: and the inspiration of the Almighty giveth them understanding."</em> — Job 32:8</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><em>"If any of you lack wisdom, let him ask of God, that giveth to all men liberally, and upbraideth not; and it shall be given him."</em> — James 1:5</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>In both Job and James, Scripture reminds us that true wisdom does not originate in human intellect, experience, rank, or age — it comes from God. Elihu understood that the wisest voices are not always the oldest, and James teaches that the humblest believer can have heaven's wisdom simply by asking. Wisdom is not earned by pride, but given through prayer. Human reasoning fails; God's Spirit illuminates. When we humble ourselves, admit our need, and seek God's guidance, He grants understanding that the world cannot produce and man cannot imitate.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>True wisdom is not learned — it is given by God to the humble who seek Him.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Solomon Asking for Wisdom (1 Kings 3:5–12).</strong> Solomon confessed weakness and lack of understanding: "I am but a little child." He asked God for an understanding heart, and God gave him wisdom beyond all men. His greatness began not with ability, but humility and prayer. Solomon became wise not because he was gifted, but because he asked.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>The Apostles Seeking Wisdom (Acts 1:14; Acts 4:31).</strong> Before leading the early church, the disciples prayed for direction. In Acts 4:31, they prayed and were filled with the Holy Ghost, and "spake the word of God with boldness." Wisdom, power, and clarity came after prayer — not before. God equips the praying believer with the wisdom needed for the work He calls them to do.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Are you facing decisions, burdens, or confusion? The Lord does not scold weakness; He supplies wisdom freely. Ask Him. Wait on Him. Listen for His voice through His Word. The same God who inspired Job and empowered James will guide you today. Human opinion confuses — God's Spirit enlightens. Prayerless minds are empty — prayerful hearts are wise.</p>
<!-- /wp:paragraph -->"""
    },
    {
        "date": "2025-10-31T08:00:00",
        "slug": "just-in-from-moldova-oct-31",
        "content": """<!-- wp:paragraph -->
<p><em>"The Spirit of God hath made me, and the breath of the Almighty hath given me life."</em> — Job 33:4</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><em>"For the law of the Spirit of life in Christ Jesus hath made me free from the law of sin and death."</em> — Romans 8:2</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>From the beginning, life has always been God-given. Elihu reminds us that every breath we take is a gift from the Almighty — not earned, not manufactured, but graciously breathed into us by God Himself. That same Spirit who formed life in us physically is the One who grants life spiritually. We were born by the breath of God, and we are born again by the Spirit of God.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Paul declares that this Spirit not only gives life, but liberty — freedom from the bondage of sin and death. In Christ, the Spirit who once animated our lungs now liberates our souls. What breath is to the body, the Holy Ghost is to the believer's spiritual life. Without Him there is suffocation; with Him, there is freedom, vitality, and spiritual strength. Let us daily walk conscious of this divine breath — grateful for physical life, and rejoicing in spiritual liberty in Christ Jesus.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Ezekiel and the Valley of Dry Bones (Ezekiel 37:1-10).</strong> Israel was like a valley of dry bones — lifeless, hopeless, and beyond human recovery. Yet when God's Spirit breathed upon them, bones came together, flesh covered them, and life surged back into them. This shows that only the Spirit of God can bring true life, revival, and restoration.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Pentecost (Acts 2:1-4).</strong> The disciples were fearful and waiting, but when the Holy Spirit came like a rushing mighty wind, they were filled with boldness, power, and life. A church hiding became a church preaching. A fearful people became a fearless witness. The same Spirit who breathed life in Job, and freedom in Romans, filled believers with power to live and speak for Christ. If God gave you breath for life, don't live like you're still chained in sin. Breathe deeply of His grace and walk in the liberty of His Spirit today.</p>
<!-- /wp:paragraph -->"""
    },
    {
        "date": "2025-11-01T08:00:00",
        "slug": "just-in-from-moldova-nov-01",
        "content": """<!-- wp:paragraph -->
<p><em>"But the hypocrites in heart heap up wrath: they cry not when he bindeth them."</em> — Job 36:13</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><em>"But after thy hardness and impenitent heart treasurest up unto thyself wrath against the day of wrath and revelation of the righteous judgment of God;"</em> — Romans 2:5</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>A heart that refuses to repent becomes a warehouse of wrath. Job warns that the hypocrite does not cry to God even when suffering, pride keeps him silent instead of repentant. Paul echoes this truth: every stubborn refusal to surrender to God is a deposit made toward future judgment.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Sin left unconfessed does not disappear, it accumulates. Silence before God is not neutrality; it is rebellion. God binds in mercy to bring us to repentance (Hosea 5:15), but when man resists, he stores up judgment instead of mercy.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Grace calls today, not tomorrow. Better to weep early than harden eternally. Every tear of repentance empties the soul of wrath and fills it with mercy.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Pharaoh (Exodus 7–14).</strong> Pharaoh hardened his heart again and again. Every plague was a chance to repent, yet he "hardened his heart" (Ex. 8:32). Instead of crying to God, he resisted God's dealings—and destruction followed. His stubborn heart stored judgment until the Red Sea buried his pride.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Judas (Matthew 26–27).</strong> Judas heard Christ's words, walked with the Truth Himself, yet never humbled his heart. Even when confronted, he did not repent, he "repented himself" (worldly sorrow), not toward God (2 Cor. 7:10). His continual rejection led to ruin. Like a bank account of rebellion, his secret sins filled up until they overflowed into tragedy.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The soft heart prays; the hard heart delays. One finds mercy; the other meets wrath. Pray today, repent today, weep today, while His grace still calls. <em>"To day if ye will hear his voice, harden not your hearts"</em> (Heb. 3:15).</p>
<!-- /wp:paragraph -->"""
    },
    {
        "date": "2025-11-02T08:00:00",
        "slug": "just-in-from-moldova-nov-02",
        "content": """<!-- wp:paragraph -->
<p><em>"Who hath put wisdom in the inward parts? or who hath given understanding to the heart?"</em> — Job 38:36</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><em>"For the LORD giveth wisdom: out of his mouth cometh knowledge and understanding."</em> — Proverbs 2:6</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Wisdom is not manufactured by man — it is given by God. In Job 38, the Lord reminds Job that all true understanding, discernment, and insight come from God placing wisdom in the heart. Man can gather information, but only God can give illumination.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Proverbs 2:6 agrees completely: the Lord alone gives wisdom, and He gives it through His Word — "out of His mouth." Human intelligence can solve problems, but only heavenly wisdom can guide a life, calm a stormed heart, or direct a believer in righteousness.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>True wisdom is not discovered by the mind — it is deposited in the heart by God. If you need direction, clarity, or discernment today, it will not come by straining harder, but by seeking the God who gives wisdom freely.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Solomon Asking for Wisdom (1 Kings 3:7–12).</strong> When Solomon became king, he confessed, "I am but a little child." He acknowledged he lacked the understanding to lead God's people. Instead of asking for riches, military strength, or long life, he asked God for "an understanding heart." God answered because Solomon recognized: Wisdom comes from God. Guidance comes from God. Discernment comes from God. God gave him "a wise and understanding heart," proving again that the Lord giveth wisdom.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Paul's Prayer for Spiritual Wisdom (Ephesians 1:17–18).</strong> Paul prayed that believers would receive "the spirit of wisdom and revelation", and that the eyes of their understanding would be enlightened. Paul knew Christians have the Bible — yet they still need God to open their understanding, illuminate truth, and guide their decisions. Just as Job 38:36 says God puts wisdom inwardly, Paul teaches that wisdom is given by the Holy Spirit, not by human effort.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Ask God daily to guide your decisions. Open His Word, because wisdom comes "out of His mouth." Trust the Spirit to enlighten your heart, not your own reasoning. When God places wisdom in the heart, He places direction in the life.</p>
<!-- /wp:paragraph -->"""
    },
    {
        "date": "2025-11-03T08:00:00",
        "slug": "just-in-from-moldova-nov-03",
        "content": """<!-- wp:paragraph -->
<p><em>"Then are they glad because they be quiet; so he bringeth them unto their desired haven."</em> — Psalm 107:30</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><em>"Then they willingly received him into the ship: and immediately the ship was at the land whither they went."</em> — John 6:21</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>When Christ enters the storm, the storm loses its power. Psalm 107 describes sailors terrified by waves that lift them "up to the heaven" and drive them "down again to the depths." But when they cry unto the Lord, He calms the storm and brings them to their desired haven. Their chaos becomes quiet, and God Himself guides the vessel.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>John 6 records the same truth in the life of the disciples. Tossed by a violent wind on the Sea of Galilee, they feared until Jesus came walking on the water. But when they "willingly received Him into the ship," Scripture says "immediately" they were at the shore. The moment Christ was welcomed, the problem ended and the destination was reached.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The principle is simple and powerful: When Christ is received, storms are quieted and progress becomes supernatural. He brings us to the place we could never reach in our own strength.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Jonah (Jonah 1–2).</strong> Jonah ran from God and brought a storm into every life around him. But when he finally called upon the Lord from the great fish, God spoke peace to the situation. The storm ceased, the fish released him, and he was placed back on the shore—exactly where God wanted him. Like Psalm 107, when Jonah cried unto the Lord, the chaos broke and the journey resumed.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Paul in the Tempest (Acts 27).</strong> Paul's ship faced a storm so severe that all hope was taken away. But Paul trusted the God "whose I am, and whom I serve." God stood by him in the night and promised deliverance. Though the ship broke apart, every soul reached land safely—God brought them to their haven. Even in destruction, Christ's presence guaranteed direction and arrival.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>When the storm is loud, invite Christ into the ship. When the winds are contrary, receive His Word willingly. When you cannot see the shore, trust the One who controls it. The same Lord who quieted Psalm 107 and carried John 6 will guide you to your "desired haven."</p>
<!-- /wp:paragraph -->"""
    },
    {
        "date": "2025-11-04T08:00:00",
        "slug": "just-in-from-moldova-nov-04",
        "content": """<!-- wp:paragraph -->
<p><em>"O ye simple, understand wisdom: and, ye fools, be ye of an understanding heart."</em> — Proverbs 8:5</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><em>"The LORD shall go forth as a mighty man, he shall stir up jealousy like a man of war: he shall cry, yea, roar; he shall prevail against his enemies."</em> — Isaiah 42:13</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Proverbs 8:5 calls the simple to gain wisdom, an invitation to listen, learn, and submit to God's truth. God never leaves the humble in ignorance; the moment a heart becomes teachable, He gives understanding.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Isaiah 42:13 shows the other side of that truth: when God's people walk in wisdom and obedience, God Himself rises as a Mighty Warrior to defend them. Wisdom leads to obedience, obedience leads to confidence, and confidence leads to seeing God fight battles we cannot fight ourselves.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Principle: When we open our hearts to God's wisdom, God opens His strength to fight on our behalf. The humble learn, and the obedient see victory.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Joshua at Jericho (Joshua 6).</strong> Joshua listened to God's instruction—though it sounded unusual (marching, trumpets, silence). Because he sought understanding and obeyed: God fought for Israel. The walls fell. The enemy was defeated. Wisdom received — obedience — God's mighty intervention.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Peter in Prison (Acts 12:5–11).</strong> Peter humbled himself, trusted God, and committed his situation to the Lord. While he was chained, guarded, and helpless: God sent an angel. The chains fell. The doors opened. Peter walked out under divine protection. A teachable, trusting heart — God rises like a mighty man of war.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>When we respond to God's call for wisdom in Proverbs 8:5, we experience the God of Isaiah 42:13 — a God who teaches the humble and defends the obedient. Wisdom opens the door to victory.</p>
<!-- /wp:paragraph -->"""
    },
    {
        "date": "2025-11-05T08:00:00",
        "slug": "just-in-from-moldova-nov-05",
        "content": """<!-- wp:paragraph -->
<p><em>"For if we have been planted together in the likeness of his death, we shall be also in the likeness of his resurrection."</em> — Romans 6:5</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><em>"And he fenced it, and gathered out the stones thereof, and planted it with the choicest vine…"</em> — Isaiah 5:2</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Both verses use the imagery of planting to show how God works in the believer's life. Isaiah 5:2 shows God preparing, protecting, and planting His people like a carefully tended vineyard. Romans 6:5 teaches that God plants us in Christ's death so He can raise us in Christ's resurrection life.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>God breaks the old ground so He can bring forth new fruit. He removes the stones of the old life and plants us into the life of Christ. Death to the old nature produces resurrection power in the new nature. When God saves a person, He does not simply repair the old life, He plants a new one. And the same God who plants is the God who prunes, protects, and produces lasting fruit.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Joseph (Genesis 39–41).</strong> Joseph was "buried" in slavery and "planted" in prison, but God was preparing him to bear fruit in Pharaoh's palace. Every painful season was God removing stones, shaping the soil, and planting Joseph exactly where he needed to be to save nations. His suffering produced spiritual fruit far greater than he could imagine. Buried in trouble — raised in triumph.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>The Seed That Dies (John 12:24).</strong> Jesus said: "Except a corn of wheat fall into the ground and die, it abideth alone…" He showed that true life always comes after a death. Christ died and rose again, and every believer who dies to the old life is planted into His resurrection power. The seed dies — the life appears.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>God plants us in Christ so we can grow in Christ. He breaks the soil, removes the stones, and buries the old man — so resurrection life can rise in its place. If God is breaking the ground, it is only because He is preparing to bring forth fruit.</p>
<!-- /wp:paragraph -->"""
    },
    {
        "date": "2025-11-06T08:00:00",
        "slug": "just-in-from-moldova-nov-06",
        "content": """<!-- wp:paragraph -->
<p>Ezekiel 9:7-8 reveals the Lord bringing Ezekiel to a hidden "hole in the wall," exposing chambers of secret idolatry. What men hid, God uncovered.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><em>"Woe unto them that seek deep to hide their counsel from the LORD…"</em> — Isaiah 29:15</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Hidden sin always becomes open shame. What we try to bury, God uncovers—not to destroy us, but to call us to repentance before judgment falls.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>God took Ezekiel step-by-step deeper into the temple, not to discourage him, but to reveal how far the people had drifted. The deeper he went, the darker it became. Hidden sin grows in secret rooms. Isaiah says men "seek deep" to hide their counsel—digging themselves into spiritual graves while imagining God cannot see. But the Lord always sees.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>He exposes not to humiliate, but to heal. He uncovers not to crush, but to cleanse. The believer must learn to keep no "chambers" the Lord cannot enter. Victory begins the moment we open the hidden rooms to His light.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Achan (Joshua 7:1–26).</strong> Achan buried his sin under a tent. He thought the dirt could hide what God already saw. His secret brought defeat to the whole nation. When exposed, he lost everything. Secret sin spreads sorrow wider than we think and ends in unavoidable exposure.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Ananias and Sapphira (Acts 5:1–11).</strong> They tried to hide part of the price, pretending deeper devotion than they possessed. Peter said they "lied to the Holy Ghost." God exposed it instantly. Hypocrisy hides nothing; God judges secret motives as clearly as open actions.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Don't let the enemy convince you that secret sin can stay hidden. Bring every chamber of your heart into the Lord's light. What we uncover in repentance, God covers in mercy. What we refuse to uncover, God will reveal in judgment.</p>
<!-- /wp:paragraph -->"""
    },
    {
        "date": "2025-11-07T08:00:00",
        "slug": "just-in-from-moldova-nov-07",
        "content": """<!-- wp:paragraph -->
<p><em>"And the Spirit of the Lord fell upon me, and said unto me, Speak; Thus saith the Lord; Thus have ye said, O house of Israel: for I know the things that come into your mind, every one of them."</em> — Ezekiel 11:5</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><em>"…for the Lord searcheth all hearts, and understandeth all the imaginations of the thoughts: if thou seek him, he will be found of thee; but if thou forsake him, he will cast thee off for ever."</em> — 1 Chronicles 28:9</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>God not only sees our actions—He searches the hidden motives behind them. The thoughts we think, the desires we hide, and the motives we justify are all laid open before Him. Nothing escapes His holy gaze. His knowledge is not to condemn but to correct and call us back to fellowship.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>When the Spirit of the Lord came upon Ezekiel, He revealed that Israel's outward worship masked inward rebellion. Likewise, David warned Solomon that God discerns the heart. True obedience begins not in public performance but in private purity. God deals with what man cannot see—what lies beneath the surface.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Achan's Hidden Sin (Joshua 7):</strong> Achan secretly took the accursed thing and buried it beneath his tent. No one saw it—but God did. His hidden greed brought defeat to Israel until it was confessed and judged. God's eye sees beneath the surface, exposing what man conceals.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Ananias and Sapphira (Acts 5:1–10):</strong> This couple pretended to give all to God, but secretly kept part back. Peter, filled with the Spirit, exposed their deceit—not because of the money withheld, but because of the lie told to the Holy Ghost. Grace is not fooled by pretense; God still searches hearts and reveals truth.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Before God, we cannot hide. But if we seek Him sincerely, He will be found of us. The same Lord who exposes our hearts also offers cleansing when we confess them. Grace reveals in order to restore.</p>
<!-- /wp:paragraph -->"""
    },
    {
        "date": "2025-11-08T08:00:00",
        "slug": "just-in-from-moldova-nov-08",
        "content": """<!-- wp:paragraph -->
<p><em>"Though Noah, Daniel, and Job, were in it, as I live, saith the Lord GOD, they shall deliver neither son nor daughter; they shall but deliver their own souls by their righteousness."</em> — Ezekiel 14:20</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><em>"Behold, the eye of the LORD is upon them that fear him, upon them that hope in his mercy; To deliver their soul from death, and to keep them alive in famine."</em> — Psalm 33:18-19</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>God's Word reminds us that faith is personal, and salvation cannot be borrowed from another's righteousness. In Ezekiel's warning, even the great men of faith—Noah, Daniel, and Job—could not save their families from judgment. Each person must personally trust and obey God.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Psalm 33 shows the balance: while judgment falls on the unbelieving, God's eye of mercy watches over those who fear Him, preserving them in famine and delivering them from death. In days of national sin or spiritual famine, faith that stands alone still finds favor before the Lord.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>God's watchful eye sees both the trembling heart and the trusting one. Even when others fall away, His mercy sustains those who walk uprightly and hope in Him alone.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Noah in the Flood (Genesis 7:1).</strong> God said to Noah, "Come thou and all thy house into the ark; for thee have I seen righteous before me in this generation." While the world mocked, Noah's personal faith secured divine protection. His obedience didn't save the world, but it saved his family. In a generation of corruption, his faith stood alone, and God remembered him (Genesis 8:1).</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>The Thief on the Cross (Luke 23:39–43).</strong> Amid mockery and rejection, one thief believed while the other blasphemed. His repentance brought immediate mercy: "Today shalt thou be with me in paradise." No one could intercede for him, he stood alone before Christ, but faith in that moment delivered his soul from eternal death. Even when the world turns from righteousness, God's eye still rests on the faithful. Personal faith brings divine favor; borrowed faith brings no deliverance. <em>"The just shall live by his faith."</em> Habakkuk 2:4.</p>
<!-- /wp:paragraph -->"""
    },
    {
        "date": "2025-11-09T08:00:00",
        "slug": "just-in-from-moldova-nov-09",
        "content": """<!-- wp:paragraph -->
<p><em>"Behold, this was the iniquity of thy sister Sodom, pride, fulness of bread, and abundance of idleness…"</em> — Ezekiel 16:49</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><em>"Though the LORD be high, yet hath he respect unto the lowly: but the proud he knoweth afar off."</em> — Psalm 138:6</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>God exposes the real root of Sodom's ruin: pride. Before the fire ever fell, their hearts were lifted. Pride produced a comfort without gratitude, prosperity without humility, and ease without seeking God. Psalm 138:6 reminds us that while the Lord is exalted above all, He draws close to the humble and keeps the proud at a distance. Pride pushes God away; humility brings Him near.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The danger of pride is not that it shouts against God—it simply lives without God. It makes a man self-sufficient, self-exalting, and self-deceived. When pride grows, spiritual sensitivity dies. God resists the proud because pride resists God. But when a heart bows low, God bends near. Humility does not earn God's presence, it removes the barrier pride builds.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>King Uzziah (2 Chronicles 26:15–21).</strong> Uzziah prospered as long as he sought the Lord, but when "his heart was lifted up to his destruction," he entered the temple proudly and was struck with leprosy. His pride pushed him far off from God's presence. God honored him when he was humble, but humbled him when he became proud.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>The Pharisee and the Publican (Luke 18:9–14).</strong> The Pharisee stood in pride, listing his righteousness. The publican stood afar off in brokenness, pleading for mercy. Jesus said the humble man went home justified, while the proud man was rejected. God drew near to the lowly but kept the proud at a distance—exactly as Psalm 138:6 declares.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Sodom fell because pride hardened their hearts. God honors the humble because humility opens the heart. Choose the posture that brings God close — bow before Him, and He will meet you there.</p>
<!-- /wp:paragraph -->"""
    },
    {
        "date": "2025-11-10T08:00:00",
        "slug": "just-in-from-moldova-nov-10",
        "content": """<!-- wp:paragraph -->
<p><em>"And all the trees of the field shall know that I the LORD have brought down the high tree, have exalted the low tree, have dried up the green tree, and have made the dry tree to flourish: I the LORD have spoken and have done it."</em> — Ezekiel 17:24</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><em>"To set up on high those that be low; that those which mourn may be exalted to safety."</em> — Job 5:11</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>In both passages, God reveals a simple, hope-filled truth: He is the One who lifts people up. He humbles the proud, but He raises the humble. When life brings us low — through discouragement, struggle, or loss — God does not abandon us there. Instead, He specializes in taking what seems dry, broken, or overlooked and causing it to flourish again. We may feel buried, but God says we are being planted. His power works best in our lowest moments, and His lifting is never accidental—it is purposeful, gentle, and always for our good.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>David the Shepherd Boy (1 Samuel 16–17).</strong> David was the youngest son, overlooked even by his own family. When Samuel came to anoint a king, David wasn't even invited to the gathering. Yet God lifted the lowly shepherd. He anointed him king and used him to defeat Goliath. David's rise shows that God delights in elevating the humble — turning the "low tree" into one that flourishes.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Mary, the Mother of Jesus (Luke 1:46–55).</strong> When Mary learned she would carry the Messiah, her song praised God because He "hath put down the mighty from their seats, and exalted them of low degree." A poor, young, unknown girl was chosen for the greatest honor in human history. Mary embodies the truth that God sees the lowly and lifts them up according to His divine purpose.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Wherever you find yourself today — low, weary, or overlooked — remember that God has not forgotten you. He is the God who causes dry trees to bloom and the humble to rise. Trust His timing, and let Him lift you in His perfect way. I know this devotion was a tough one — especially for me. Thank God for The King James Bible because it humbles us.</p>
<!-- /wp:paragraph -->"""
    },
    {
        "date": "2025-11-11T08:00:00",
        "slug": "just-in-from-moldova-nov-11",
        "content": """<!-- wp:paragraph -->
<p><em>"The soul that sinneth, it shall die. The son shall not bear the iniquity of the father, neither shall the father bear the iniquity of the son: the righteousness of the righteous shall be upon him, and the wickedness of the wicked shall be upon him."</em> — Ezekiel 18:20</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><em>"For the Son of man shall come in the glory of his Father with his angels; and then he shall reward every man according to his works."</em> — Matthew 16:27</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>God makes it clear in both the Old and New Testament that every individual is accountable for their own choices, own conduct, and own walk with Him.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Ezekiel emphasizes personal responsibility—no one can blame another person for their sin, nor can anyone borrow another person's righteousness. Matthew emphasizes personal reward—Christ Himself will judge every man not by excuses or associations, but by what he did with the light he was given.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>You cannot stand on someone else's obedience. You cannot hide behind someone else's failures. You cannot escape your own choices, nor can you lose the reward for another person's compromise. God's message is simple: Your walk is your own. Your choices matter. Your rewards will be personal. The grace of God saves us, but the judgment seat of Christ will examine the life we lived, the motives we carried, and the steps we chose.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Achan (Joshua 7).</strong> Achan's sin was hidden, but God held Achan personally accountable. The nation suffered temporarily, but the guilt was his alone. He could not blame the crowd, the circumstances, or the pressure. His personal disobedience produced personal consequences. Ezekiel's message is seen clearly: "the wickedness of the wicked shall be upon him."</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Ananias and Sapphira (Acts 5).</strong> Ananias and Sapphira chose to lie to the Holy Ghost. Though a married couple, God judged each individually: Ananias fell dead for his deception. Moments later, Sapphira fell for her own agreement with sin. They stood before God separately. Their accountability was personal and unavoidable. This illustrates Jesus' teaching: "He shall reward every man according to his works."</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Every choice you make leaves a trail. Every step you take builds your spiritual future. Every decision is recorded in heaven. You cannot change yesterday, but by God's mercy you can obey today — and today's obedience will shape tomorrow's reward. Walk humbly. Choose wisely. Live responsibly before God.</p>
<!-- /wp:paragraph -->"""
    },
    {
        "date": "2025-11-12T08:00:00",
        "slug": "just-in-from-moldova-nov-12",
        "content": """<!-- wp:paragraph -->
<p><em>"The LORD preserveth the simple: I was brought low, and he helped me."</em> — Psalm 116:6</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><em>"For your obedience is come abroad unto all men. I am glad therefore on your behalf: but yet I would have you wise unto that which is good, and simple concerning evil."</em> — Romans 16:19</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Both passages show a powerful truth for believers: God protects the believer whose heart stays simple, humble, and clean from evil. To be simple in Scripture does not mean ignorant; it means: humble, teachable, without deceit, without double motives, easily guided by the Word, avoiding the complexity of sin.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The psalmist said he was "brought low"—a place of weakness—yet God preserved him because his heart was simple, leaning wholly on the Lord. Paul, in Romans, calls believers to be: wise in good — know truth deeply. Simple concerning evil — don't explore, taste, study, or flirt with sin. A heart that stays clean from evil stays under God's preserving hand. The safest life is the simplest life — one that stays far from evil and close to the Shepherd.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Joseph (Genesis 39).</strong> Joseph was surrounded by the corrupt culture of Egypt, yet he stayed simple concerning evil. When Potiphar's wife tempted him, Joseph did NOT: debate the temptation, entertain the idea, reason through it, study the situation. He ran. Why? Because he kept himself simple concerning evil. And because of that simplicity, "The LORD was with Joseph" (Gen. 39:21). God preserved him because he kept his heart clean.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Timothy (2 Timothy 3:14–17).</strong> Paul reminded Timothy: you learned the Scriptures from a child, you stayed away from false teachers, you held to the Word, you avoided corrupt doctrines and evil practices. Timothy kept a simple, pure devotion to Scripture and truth. He didn't chase deep philosophies or heresies. Because of that, Paul called him a faithful servant, and God used him greatly in the early church. Like Timothy, the believer who stays simple, grounded, and humble is preserved by God and kept from corruption.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The world says being "simple" is weakness. God says being "simple concerning evil" is strength. A humble heart God preserves. A clean heart God protects. A simple heart God helps. Stay wise in what is good. Stay simple in what is evil. And the Lord will preserve you.</p>
<!-- /wp:paragraph -->"""
    },
    {
        "date": "2025-11-13T08:00:00",
        "slug": "just-in-from-moldova-nov-13",
        "content": """<!-- wp:paragraph -->
<p><em>"The spirit of a man will sustain his infirmity; but a wounded spirit who can bear?"</em> — Proverbs 18:14</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><em>"So that contrariwise ye ought rather to forgive him, and comfort him, lest perhaps such a one should be swallowed up with overmuch sorrow."</em> — 2 Corinthians 2:7</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The strongest believers can endure outward trials when their spirit is strong, anchored in the Lord. But when the inner life is crushed—when guilt, grief, or failure wound the heart—no amount of human strength can carry a person. A wounded spirit is the deepest kind of hurt.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>This is why Paul urges the church to comfort and restore the fallen brother in Corinth. The man had repented. Now he needed forgiveness, not further rejection. Without it, he would be "swallowed up with overmuch sorrow." A wounded spirit needs mercy. A restored spirit needs grace. God's desire is that His people lift the fallen, not leave them there.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>A wounded spirit cannot survive without grace, forgiveness, and comfort, and God calls His people to be instruments of that restoration.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>David After His Sin (2 Samuel 12; Psalm 51).</strong> David's sin with Bathsheba crushed his spirit. Nathan the prophet confronted him, and David immediately confessed. Yet the deepest agony he expressed was not the consequences to his kingdom, but the wounding of his spirit. In Psalm 51 he cries: "Restore unto me the joy of thy salvation…" (Psalm 51:12). Even a man "after God's own heart" could not stand under the weight of a broken spirit. God forgave him and restored him, showing that mercy heals where judgment alone cannot. Just as Paul urged the Corinthians to comfort the repentant, Nathan's confrontation was followed by clear assurance of God's forgiveness: "The Lord also hath put away thy sin…" (2 Samuel 12:13). Grace lifted David's wounded spirit.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Peter After Denial (John 21:15–17).</strong> Peter's spirit was shattered when he denied Christ three times. His failure wounded him more deeply than prison or persecution ever could. But the risen Christ came personally to restore him. Three denials. Three questions. Three affirmations of love and renewed calling. Christ did not crush Peter—He comforted him, lifted him out of despair, and restored him to ministry. This matches Paul's teaching perfectly: Forgive. Comfort. Restore. Lift the wounded spirit.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Someone near you may be carrying a wounded spirit—broken by sin, grief, fear, or failure. The Lord may call you to be the one who: Forgives freely, Comforts sincerely, Restores gently, Lifts compassionately. Because what Proverbs asks—"A wounded spirit who can bear?"—Paul answers: The church, filled with the grace of Christ, can lift that wounded soul.</p>
<!-- /wp:paragraph -->"""
    },
    {
        "date": "2025-11-14T08:00:00",
        "slug": "just-in-from-moldova-nov-14",
        "content": """<!-- wp:paragraph -->
<p><em>"I called upon the LORD in distress: the LORD answered me, and set me in a large place."</em> — Psalm 118:5</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><em>"And hast not shut me up into the hand of the enemy: thou hast set my feet in a large room."</em> — Psalm 31:8</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Both psalms declare the same truth: God brings His people out of tight, fearful places and sets them into a place of freedom, safety, and spiritual enlargement. The "distress" describes a narrow, suffocating place — fear closing in, pressures tightening, enemies surrounding, no human escape.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But when the believer calls on the Lord, God enlarges the soul before He enlarges the situation. He brings us: from fear to faith, from pressure to peace, from confinement to confidence, from darkness to deliverance. God has a way of opening doors no man can shut (Revelation 3:7).</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Joseph Lifted Out of the Prison (Genesis 41).</strong> Joseph knew the "narrow place" well — forgotten, betrayed, falsely accused. But in one day, God brought him out of the deepest confinement and set him in the broadest place in Egypt. From a prison cell to the palace. From irons on his feet to a ring on his hand. From distress to enlargement. Joseph lived Psalm 118:5.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Peter Freed from the Prison Cell (Acts 12:6–11).</strong> Peter was chained between soldiers. Doors, guards, iron gates — a narrow place with no human escape. But the angel of the Lord awakened him, loosed the chains, opened the gates, and brought him into the city—a large place of freedom. Peter declared: "Now I know of a surety…" (Acts 12:11). God made the impossible path open before him. Psalm 31:8 in action.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Whatever tight place you feel trapped in today — fear, pressure, sickness, financial strain, emotional heaviness — call upon the Lord. The God who enlarged Joseph's steps and opened Peter's prison can bring you out into a "large place" of: renewed hope, renewed strength, renewed confidence, renewed freedom. Your distress is not your destiny. God is preparing a broader place for you.</p>
<!-- /wp:paragraph -->"""
    },
]

results = []
total = len(entries)
for i, entry in enumerate(entries):
    data = {
        "title": "Just in From Moldova",
        "content": entry["content"],
        "status": "publish",
        "date": entry["date"],
        "categories": [43],
        "author": 16,
        "slug": entry["slug"]
    }
    body = json.dumps(data)
    try:
        proc = subprocess.run(
            ["curl", "-s", "-X", "POST", WP_URL,
             "-u", f"{USER}:{PASS}",
             "-H", "Content-Type: application/json",
             "-d", body],
            capture_output=True, text=True, timeout=30
        )
        result = json.loads(proc.stdout)
        post_id = result.get("id", "N/A")
        if post_id != "N/A":
            results.append({"date": entry["date"][:10], "id": post_id, "slug": entry["slug"], "status": "OK"})
            print(f"[{i+1}/{total}] Posted {entry['date'][:10]} -> ID {post_id}")
        else:
            msg = result.get("message", "Unknown error")
            results.append({"date": entry["date"][:10], "slug": entry["slug"], "status": f"ERROR: {msg}"})
            print(f"[{i+1}/{total}] FAILED {entry['date'][:10]}: {msg}")
    except Exception as e:
        results.append({"date": entry["date"][:10], "slug": entry["slug"], "status": f"ERROR: {e}"})
        print(f"[{i+1}/{total}] FAILED {entry['date'][:10]}: {e}")
    time.sleep(0.5)

print(f"\n=== SUMMARY ===")
ok = [r for r in results if r["status"] == "OK"]
fail = [r for r in results if r["status"] != "OK"]
print(f"Success: {len(ok)}, Failed: {len(fail)}")
for r in results:
    print(f"  {r['date']} | ID: {r.get('id','N/A')} | {r['status']}")
