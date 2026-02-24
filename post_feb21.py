#!/usr/bin/env python3
import subprocess, json

title = "Just in From Moldova – February 21, 2026"
slug = "manna-feb-21-2026"

content = (
'<!-- wp:paragraph -->\n'
'<p><em>"There is a river, the streams whereof shall make glad the city of God, the holy place of the tabernacles of the most High."</em> — <strong>Psalm 46:4</strong></p>\n'
'<!-- /wp:paragraph -->\n\n'
'<!-- wp:paragraph -->\n'
'<p><em>"O that thou hadst hearkened to my commandments! then had thy peace been as a river, and thy righteousness as the waves of the sea."</em> — <strong>Isaiah 48:18</strong></p>\n'
'<!-- /wp:paragraph -->\n\n'
'<!-- wp:paragraph -->\n'
'<p>In Psalm 46, Jerusalem had no natural river, yet God declares, "There is a river." That river was not geographical — it was spiritual. It represents the steady, sustaining presence of God in the midst of trouble.</p>\n'
'<!-- /wp:paragraph -->\n\n'
'<!-- wp:paragraph -->\n'
'<p>Isaiah 48:18 shows us why many never experience that river. The Lord says, "O that thou hadst hearkened…" Peace flows where obedience lives. When we resist His commandments, we dam up the river ourselves.</p>\n'
'<!-- /wp:paragraph -->\n\n'
'<!-- wp:paragraph -->\n'
"<p><strong>God's peace is not a puddle that evaporates under pressure. It is a river — constant, flowing, sustaining — but it flows strongest in the channel of obedience.</strong></p>\n"
'<!-- /wp:paragraph -->\n\n'
'<!-- wp:separator -->\n<hr class="wp-block-separator"/>\n<!-- /wp:separator -->\n\n'
'<!-- wp:heading {"level":3} -->\n<h3>Hezekiah\'s Hidden River</h3>\n<!-- /wp:heading -->\n\n'
'<!-- wp:paragraph -->\n'
'<p>When Sennacherib came against Jerusalem, King Hezekiah stopped the outward water sources and redirected the water underground into the city (2 Kings 20:20; 2 Chronicles 32:3-4). Jerusalem survived the siege because there was a hidden supply. The enemy could surround the city, but he could not stop the river.</p>\n'
'<!-- /wp:paragraph -->\n\n'
'<!-- wp:paragraph -->\n'
'<p>So it is with the obedient believer: Trouble may surround you. Pressures may increase. Enemies may threaten. But if you are walking in obedience, there is a hidden river flowing within — and the enemy cannot cut off that supply.</p>\n'
'<!-- /wp:paragraph -->\n\n'
'<!-- wp:separator -->\n<hr class="wp-block-separator"/>\n<!-- /wp:separator -->\n\n'
'<!-- wp:heading {"level":3} -->\n<h3>Paul and Silas in Prison</h3>\n<!-- /wp:heading -->\n\n'
'<!-- wp:paragraph -->\n'
'<p>In Acts 16:25, Paul and Silas were beaten and placed in the inner prison. Yet at midnight, they prayed and sang praises unto God. <strong>That is river peace.</strong></p>\n'
'<!-- /wp:paragraph -->\n\n'
'<!-- wp:paragraph -->\n'
"<p>Their backs were bleeding. Their feet were in stocks. But the river was still flowing. Why? Because they were in the center of God's will. Obedience produced peace — even in prison. The earthquake that followed did not create the peace. It revealed the power of it.</p>\n"
'<!-- /wp:paragraph -->\n\n'
'<!-- wp:paragraph -->\n'
'<p><strong>Peace is not the absence of conflict. Peace is the presence of God flowing through obedience.</strong> When we hearken, peace flows. When we resist, peace dries. A mission field like Moldova — surrounded by instability, economic pressures, and regional tensions — yet the church can still have a river. Because the river is not political. It is not circumstantial. It is spiritual. And it flows strongest where there is obedience.</p>\n'
'<!-- /wp:paragraph -->\n\n'
'<!-- wp:separator -->\n<hr class="wp-block-separator"/>\n<!-- /wp:separator -->\n\n'
'<!-- wp:heading {"level":3} -->\n<h3>Mission Report Update</h3>\n<!-- /wp:heading -->\n\n'
'<!-- wp:paragraph -->\n'
'<p>Greetings in the precious name of our Lord Jesus Christ.</p>\n'
'<!-- /wp:paragraph -->\n\n'
'<!-- wp:paragraph -->\n'
"<p>We are grateful to report the Lord's continued blessings upon the ministry this month here in Moldova and beyond. Even in difficult regions and uncertain times, the Word of God is not bound.</p>\n"
'<!-- /wp:paragraph -->\n\n'
'<!-- wp:paragraph -->\n'
'<p>One of our greatest joys this month was seeing <strong>Alexander, a 13-year-old boy from a refugee family living in Prednistrovia</strong> — a Russian republic within the borders of Moldova — <strong>trust Christ as his Saviour.</strong> These displaced families have endured much uncertainty, yet the Gospel continues to bring eternal hope. Please rejoice with us that another soul has been rescued by the grace of God.</p>\n'
'<!-- /wp:paragraph -->\n\n'
'<!-- wp:paragraph -->\n'
'<p>The Lord has also opened wide doors for literature distribution:</p>\n'
'<!-- /wp:paragraph -->\n\n'
'<!-- wp:list -->\n'
'<ul>\n'
'<li>We printed <strong>10,000 John and Romans</strong> through Bible Baptist Church in Chisinau, Moldova. These were shipped to churches and contacts in <strong>The Netherlands and Belgium</strong>, where they are being used for evangelism and outreach.</li>\n'
'<li>Books and gospel tracts were shipped to <strong>three churches in Poland</strong> ministering specifically to Russian-speaking families displaced because of the war.</li>\n'
'<li>We are sending two large shipments of books and tracts to <strong>Chita, Russia</strong>, where believers are continuing to distribute Scripture faithfully despite the challenges.</li>\n'
'<li>Two large shipments of books were sent to <strong>New Moldova in Romania</strong>, strengthening the churches and believers there.</li>\n'
'</ul>\n'
'<!-- /wp:list -->\n\n'
'<!-- wp:paragraph -->\n'
'<p>At present, we have <strong>eight churches</strong> within our ministry faithfully preaching and teaching the Word of God. We thank the Lord for pastors and believers who stand firm in doctrine and continue the work of evangelism and discipleship in their regions.</p>\n'
'<!-- /wp:paragraph -->\n\n'
'<!-- wp:paragraph -->\n'
'<p>We are reminded again that the printed page travels where we cannot always go. Each John and Romans, each book, each tract represents a seed sown into hearts across Europe and beyond.</p>\n'
'<!-- /wp:paragraph -->\n\n'
'<!-- wp:paragraph -->\n'
'<p>Thank you for your prayers and faithful support. Your partnership enables us to continue reaching refugees, strengthening churches, and sending the Gospel across borders.</p>\n'
'<!-- /wp:paragraph -->\n\n'
'<!-- wp:paragraph -->\n'
'<p><strong>Please continue to pray:</strong></p>\n'
'<!-- /wp:paragraph -->\n\n'
'<!-- wp:list -->\n'
'<ul>\n'
"<li>For Alexander's spiritual growth.</li>\n"
'<li>For protection and boldness for believers in Russia and Eastern Europe.</li>\n'
'<li>For the continued printing and distribution of Scripture.</li>\n'
'<li>For the eight churches under our care to remain steadfast and fruitful.</li>\n'
'</ul>\n'
'<!-- /wp:list -->\n\n'
'<!-- wp:paragraph -->\n'
'<p>We are grateful for you and for your investment in eternal things.</p>\n'
'<!-- /wp:paragraph -->\n\n'
'<!-- wp:paragraph -->\n'
'<p>Sincerely in Christ,<br><strong>Pastor Paul Hamilton</strong><br>Bible Baptist Church Moldova<br>Biblebaptistchurchmoldova.com</p>\n'
'<!-- /wp:paragraph -->'
)

payload = json.dumps({
    "title": title,
    "content": content,
    "status": "publish",
    "slug": slug,
    "categories": [43],
    "author": 16,
    "date": "2026-02-21T06:00:00"
})

proc = subprocess.run(
    ["curl", "-s", "-X", "POST", "https://joequick.com/wp-json/wp/v2/posts",
     "-u", "joe.quick:A4eZRwAwtv1HN9gQz7pk3Yae",
     "-H", "Content-Type: application/json",
     "-d", payload],
    capture_output=True, text=True, timeout=30
)

try:
    resp = json.loads(proc.stdout)
    print(f"ID: {resp.get('id')}")
    print(f"Link: {resp.get('link')}")
    print(f"Status: {resp.get('status')}")
except:
    print(f"Error: {proc.stdout[:300]}")
    print(f"Stderr: {proc.stderr[:300]}")
