# Tutan Öngörüler (Vitrin)

Utku Şen'in S.A.H yayınlarında önceden haber verip haklı çıktığı tahminler.

> **Genel Durum:** 🟢 Tuttu: **3** | 🟡 Kısmen Tuttu: **3** | 🔴 Tutmadı: **4** | ⚪ Belirsiz: **2**

---

## <span class="badge-kismen">KISMEN TUTTU</span> | 50.bölüm özel intro, haftada 4 gün çalışma, rusya'dan saldırılar -siber alemden havadisler 50. bölüm | 📅 2022-02-18
### 3. Utku, mavi takım (Blue Team / SOC) rollerinin asla bitmeyeceğini fakat ekiplerin çalışma odağının geleneksel şirket içi Active Directory yapılarından tamamen bulut (cloud) altyapılarına ve bulut log analizine kayacağını söylüyor.
- **Sonuç:** <span class="badge-kismen">KISMEN TUTTU</span> (Güven Skoru: **5.4/10**)
- **Olasılık Dağılımı:** `KISMEN TUTTU: %54.0 | TUTTU: %41.9 | TUTMADI: %0.6 | BELIRSIZ: %3.5`
- **Videoda Ne Demişti:** Bir izleyicinin Blue Team ve SOC tarafının geleceği olup olmadığı yönündeki sorusunu yanıtlayan Utku Şen, savunma tarafının asla ölmeyeceğini vurguluyor. Ancak ekiplerin odak noktasının değiştiğini, eskiden Active Directory ağırlıklı çalışan mavi takımların artık tamamen bulut ortamındaki saldırıları ve logları incelemeye evrildiğini kendi gözlemi ve tahmini olarak dile getiriyor.
- **İncelenen Web Kanıtları:**
  - `[Tavily]` [From On-Prem Active Directory to Cloud-Native Entra ID: Why IT Teams Are Making the Shift - BitTitan MigrationWiz](https://www.bittitan.com/blog/from-the-experts/from-on-prem-active-directory-to-cloud-native-entra-id-why-it-teams-are-making-the-shift)
    > 💬 *"March 24, 2026 For decades, on-premises Active Directory (AD) has been the backbone of identity and device management in enterprise environments. But as infrastructure, applications, and users increasingly move beyond the traditional network perimeter, the limitations of legacy AD become more pronounced. IT teams are now under pressure to support distributed workforces, strengthen security posture..."*
  - `[Tavily]` [Microsoft Urges Organizations to Move Beyond Active Directory](https://petri.com/microsoft-organizations-move-beyond-active-directory)
    > 💬 *"Microsoft advises a gradual modernization approach rather than a complete replacement of Active Directory. IT teams should begin by moving authentication and access controls to cloud-based identity platforms, adopting stronger sign-in methods such as phishing-resistant authentication, and reducing dependence on outdated authentication protocols. Moreover, access decisions should also be based on r..."*
  - `[Tavily]` [Road to the cloud - Move identity and access management from Active Directory Domain Services (AD DS) to a Microsoft Entra migration workstream - Microsoft Entra | Microsoft Learn](https://learn.microsoft.com/en-us/entra/architecture/road-to-the-cloud-migrate)
    > 💬 *"After you align your organization toward halting growth of the Active Directory Domain Services (AD DS) footprint, you can focus on moving the existing on-premises workloads to Microsoft Entra ID. This article describes the various migration workstreams. You can execute the workstreams in this article based on your priorities and resources. A typical migration workstream has the following stages: ..."*
  - `[Tavily]` [Migrating From AD to Entra ID - How to Successfully Navigate the Cloud Transformation Journey](https://www.youtube.com/watch?v=L78nU6DzdKw)
    > 💬 *"### Description 16,830 views Posted: 2024-12-10 If your organization is looking for guidance on the cloud-native Identity and Access Management (IAM) environment, join this session! Our Product Managers from the Microsoft Identity and Network Access engineering team will walk you through the key milestones and recommendations of the Cloud journey from Active Directory to Microsoft Entra ID. You wi..."*
  - `[DuckDuckGo]` [Active Directory Auditor - AD Security Tool](https://www.bing.com/aclick?ld=e84KLKFqOOoUC5xl0hC9LhfzVUCUxTlt4dZfmEkTeE6gMHY75UFkfkweJ88mhlHB3WXquMIzXQPHiMLe1xC1CnbEiCAmC9cmRYzT81WgO8FS_oZbmSdAanaTfJRBzUzbQW6aF4Ac-EKQJPmrzsoxlBGLHTHExPbpq2VqXTb019tBWoxwgAVBseDw3oRDe4Zj6ai06EJsxpycltiOUAh1mZDm4AASA&u=aHR0cHMlM2ElMmYlMmZ3d3cubWFuYWdlZW5naW5lLmNvbSUyZnByb2R1Y3RzJTJmYWN0aXZlLWRpcmVjdG9yeS1hdWRpdCUyZnNlbSUyZmxwJTJmYWN0aXZlLWRpcmVjdG9yeS1hdWRpdGluZy5odG1sJTNmY2FtaWQlM2Q0NzEzMTkxMjclMjZhZGdpZCUzZDEzMDI5MjI0ODgxNTI3MjclMjZrd2QlM2RhZCUyNTIwdG9vbCUyNm1hdGNodHlwZSUzZHAlMjZhZGlkJTNkJTI2bmV0d29yayUzZG8lMjZhZHBvc2l0aW9uJTNkJTI2bG9jJTNkMTM4MDcyJTI2cGxhY2VtZW50JTNkJTI2dGFyZ2V0JTNkJTI2c2VhcmNocXVlcnklM2RibHVlJTI1MjB0ZWFtJTI1MjBzaGlmdCUyNTIwZnJvbSUyNTIwYWN0aXZlJTI1MjBkaXJlY3RvcnklMjUyMGNsb3VkJTI2bXNjbGtpZCUzZGU5Nzg5YTIzNDViYjE2ODg1NTMwZjBkODBmMTQwMmJhJTI2dXRtX3NvdXJjZSUzZGJpbmclMjZ1dG1fbWVkaXVtJTNkY3BjJTI2dXRtX2NhbXBhaWduJTNkQURBUCUyNTIwU2VhcmNoJTI1MjBUdXJrZXklMjUyMC0lMjUyMEltcCUyNnV0bV90ZXJtJTNkYWQlMjUyMHRvb2wlMjZ1dG1fY29udGVudCUzZEFEJTI1MjBBdWRpdCUyNTIwVG9vbA&rlid=e9789a2345bb16885530f0d80f1402ba)
    > 💬 *"Analyze the root-cause of your critical AD changes from detailed reports of ADAudit plus. It gives you a centralized view of your systems, so that you can track and monitor users"*

---

## <span class="badge-tuttu">TUTTU</span> | AB'den teknoloji tekellerine çelme, cybertakeoff sınavında sorun -siber alemden havadisler 55. bölüm | 📅 2022-04-01
### 3. Utku, Okta raporunu sızdırdığı için Zoom'dan kovulan genç araştırmacı Bill Demirkapı'nın siber güvenlik tarihinin en büyük dahilerinden biri olduğunu ve gelecekte sektörde çok önemli yerlere geleceğini söylüyor.
- **Sonuç:** <span class="badge-tuttu">TUTTU</span> (Güven Skoru: **8.0/10**)
- **Olasılık Dağılımı:** `TUTTU: %80.4 | TUTMADI: %0.5 | KISMEN TUTTU: %16.2 | BELIRSIZ: %2.9`
- **Videoda Ne Demişti:** Okta'nın hacklenme sürecine dair Mandiant raporunu paylaştığı için Zoom tarafından işine son verilen Bill Demirkapı olayını yorumlayan Utku Şen, Zoom'un çok büyük bir aptallık yaptığını söylüyor. Bu kalibredeki yetenekleri şirketlerin değil bizzat araştırmacıların seçtiğini belirterek Bill'in ileride çok büyük başarılara imza atacağını kendi inancı ve tahmini olarak dile getiriyor.
- **İncelenen Web Kanıtları:**
  - `[Tavily]` [Thousands of Corporate Secrets Were Left Exposed. This Guy Found Them All | WIRED](https://www.wired.com/story/secret-hunting-bill-demirkapi)
    > 💬 *"If you know where to look, plenty of secrets can be found online. Since the fall of 2021, independent security researcher Bill Demirkapi has been building ways to tap into huge data sources, which are often overlooked by researchers, to find masses of security problems. This includes automatically finding developer secrets—such as passwords, API keys, and authentication tokens—that could give cybe..."*
  - `[Tavily]` [Bill Demirkapi](https://linkedin.com/in/bill-demirkapi-171054135)
    > 💬 *"# Bill Demirkapi Headline: Member of Technical Staff Current role: Member Of Technical Staff Seniority: Specialist, Engineering and Technical Location: San Francisco, California, United States Experience: 6 years 5 months LinkedIn: www.linkedin.com/in/bill-demirkapi-171054135 · 1,576 followers Description: Hi 👋, my name is Bill Demirkapi, and I'm a researcher with a passion for scaling security. [..."*
  - `[Tavily]` [Bill Demirkapi's Blog](https://billdemirkapi.me)
    > 💬 *"In May, I published a blog post detailing a Remote Code Execution vulnerability in Dell SupportAssist. Since then, my research has continued and I have been finding more and more vulnerabilities. I strongly suggest that you read my previous blog post, not only because it provides a solid conceptual understanding Remote Code Execution on most Dell computers Security Research ## Remote Code Executio..."*
  - `[Tavily]` [Secrets and Shadows: Leveraging Big Data for Vulnerability Discovery at Scale](https://billdemirkapi.me/leveraging-big-data-for-vulnerability-discovery-at-scale)
    > 💬 *"Security Research # Secrets and Shadows: Leveraging Big Data for Vulnerability Discovery at Scale Modern technologies like the cloud have made rapidly developing scalable software more accessible than ever. What risks has cloud computing introduced for the sake of convenience? Bill Demirkapi #### Bill Demirkapi • 36 min read Secrets and Shadows: Leveraging Big Data for Vulnerability Discovery at S..."*
  - `[DuckDuckGo]` [Bill Demirkapi - grokipedia.com](https://grokipedia.com/page/bill-demirkapi)
    > 💬 *"Bill Demirkapi has established himself as an independent security researcher through self-directed investigations into system vulnerabilities, often leveraging publicly available or leaked data to probe for weaknesses beyond his professional duties at Microsoft."*

---

## <span class="badge-kismen">KISMEN TUTTU</span> | ABD Devleti, 19 Yaşındaki Hacker Çocuğa Emanet - S.A.H E113 | 📅 2025-02-09
### 1. Utku, yapay zekanın ses ve görüntü gecikmelerinin her geçen gün azalarak sahteciliğin anlaşılmaz hale geleceğini, bu suistimaller yüzünden uzaktan mülakatların tarihe karışacağını ve şirketlerin herkesi mecburen ofise çağıracağını söylüyor.
- **Sonuç:** <span class="badge-kismen">KISMEN TUTTU</span> (Güven Skoru: **6.5/10**)
- **Olasılık Dağılımı:** `KISMEN TUTTU: %64.9 | TUTMADI: %2.3 | TUTTU: %24.5 | BELIRSIZ: %8.2`
- **Videoda Ne Demişti:** Adayların iş mülakatlarında arka planda yapay zeka ve deepfake kullanmasını kendi işe alım tecrübesi üzerinden anlatan Utku Şen, bu teknolojilerin hızla geliştiğini ve gecikmelerin yakında tamamen kaybolacağını vurguluyor. Uzaktan mülakatın çok daha pratik olduğunu ancak bu sahtecilikler nedeniyle ileride tamamen biteceğini kendi tahmini olarak ekliyor.
- **İncelenen Web Kanıtları:**
  - `[Tavily]` [AI Is Forcing the Return of the In-Person Job Interview: Here’s Why It’s Actually a Good Thing | Gogotechy](https://gogotechy.com/blog/ai-is-forcing-the-return-of-the-in-person-job-interview)
    > 💬 *"Yes, AI is forcing the return of the in-person job interview. Major companies in the U.S. are returning to in-person interviews to combat the use of AI for cheating, such as generating answers or even impersonating candidates during virtual interviews. This trend is a direct reaction to AI tools making it easier for job seekers to appear more skilled than they really are. According to a recent Wal..."*
  - `[Tavily]` [To counter AI cheating, companies bring back in-person job interviews – Computerworld](https://www.computerworld.com/article/4044734/to-counter-ai-cheating-companies-bring-back-in-person-job-interviews.html)
    > 💬 *"AI-enabled cheating has surged, particularly in virtual technical job interviews. Would-be job candidates increasingly use AI tools off-camera to feed them answers, such as responses to coding challenges, and in some cases turning to deepfake technology to impersonate applicants. To battle that trend, more and more companies are ditching screens for handshakes — bringing back in-person job intervi..."*
  - `[Tavily]` [AI cheating in interviews: the 2026 state of play (and what to actually do about it) - Expert Hire Blog](https://www.experthire.io/blog/ai-cheating-in-interviews)
    > 💬 *"Hiring teams are starting to react, unevenly. Google's Sundar Pichai reportedly told an internal town hall in February 2025 that the company would return to in-person interviews for some roles to address the rise in candidates using AI in interviews, and Deloitte reinstated in-person interviews for parts of its UK graduate program. Specific founder anecdotes circulating in 2026 include one technol..."*
  - `[Tavily]` [AI Is Bringing Back In-Person Job Interviews - WSJ](https://www.wsj.com/lifestyle/careers/ai-job-interview-virtual-in-person-305f9fd0)
    > 💬 *"Virtual interviews have become the new normal in hiring in recent years, driven by the rise of remote work and companies’ desire to speed up hiring. Trouble is, more candidates are using AI tools to cheat by feeding them answers off screen, especially in technical interviews, recruiters say. In rarer cases, AI-enabled scammers are impersonating job seekers with the aim of stealing data or money on..."*
  - `[DuckDuckGo]` [In-Person Interviews Make a Comeback to Combat AI Fraud](https://blog.theinterviewguys.com/in-person-interviews-make-a-comeback/)
    > 💬 *"Jun 25, 2026 · In this article, you’ll discover how companies like Google, Cisco, and McKinsey are responding to AI fraud, why in-person interviews are making a strategic comeback, and most importantly, how this shift creates new opportunities for authentic job seekers to stand out."*

---

## <span class="badge-tuttu">TUTTU</span> | ABD Devleti, 19 Yaşındaki Hacker Çocuğa Emanet - S.A.H E113 | 📅 2025-02-09
### 2. Utku, devletle özel sektörü ayıran disiplin ve kuralcılığın ortadan kalkmasıyla kamu veri tabanlarının genç hackerlara açılmasının sonunun çok kötü olacağını, devlet ciddiyetinin zayıflamasının büyük bir felakete yol açacağını söylüyor.
- **Sonuç:** <span class="badge-tuttu">TUTTU</span> (Güven Skoru: **6.7/10**)
- **Olasılık Dağılımı:** `KISMEN TUTTU: %25.9 | TUTMADI: %2.9 | BELIRSIZ: %4.2 | TUTTU: %67.0`
- **Videoda Ne Demişti:** Elon Musk'ın DOGE yapılanmasına 19 yaşında yeraltı hacker bağlantıları olan bir genci dahil edip devlet veri tabanlarına yetki vermesini değerlendiren Utku Şen, çocuk yaştaki hackerlara sınırsız yetki verilmesinin kırmızı çizgiyi aştığını belirtiyor. Devlet ciddiyetinin yok olduğu ve disiplinin kaybolduğu bu gidişatın sonunun asla iyi bir yere varmayacağını kendi endişesi ve öngörüsü olarak paylaşıyor.
- **İncelenen Web Kanıtları:**
  - `[Tavily]` [DOGE Put Critical Social Security Data at Risk, Whistle-Blower Says](https://www.congress.gov/119/meeting/house/118875/documents/HHRG-119-JU13-20260121-SD002-U2.pdf)
    > 💬 *"The account by the whistle-blower, Charles Borges, underscores concerns that have led to lawsuits seeking to block young software engineers at the agency built by Elon Musk from having access to confidential government data. In his complaint, Mr. Borges said DOGE members copied the data to an internal agency server that only DOGE could access, forgoing the type of “independent security monitoring”..."*
  - `[Tavily]` [DOGE is putting the country’s data and computing infrastructure at risk, HKS expert argues | Harvard Kennedy School](https://www.hks.harvard.edu/faculty-research/policy-topics/science-technology-data/doge-putting-countrys-data-and-computing)
    > 💬 *"are the effects of DOGE’s unprecedent access to many highly sensitive federal databases and payment tools. Bruce Schneier, a security technologist and lecturer at the Kennedy School, wrote about this for The Atlantic and Foreign Policy. We spoke with him to learn more about the risks to federal data. [...] These government systems are now less secure than they were because of DOGE’s actions. And h..."*
  - `[Tavily]` [Ranking Member Robert Garcia Expands DOGE Social Security Data Leak Investigation Following Explosive New Whistleblower Allegations | The U.S. House Committee on Oversight](https://oversightdemocrats.house.gov/news/press-releases/ranking-member-robert-garcia-expands-doge-social-security-data-leak-investigation-following-explosive-new-whistleblower-allegations)
    > 💬 *"In September 2025, Ranking Member Garcia sent a letter to the Acting Inspector General at the Social Security Administration demanding an investigation after a whistleblower revealed claims that members of DOGE copied the entire Social Security database, which contains the sensitive personal information of over 300 million Americans, and illegally moved the information to an unsecure cloud server ..."*
  - `[Tavily]` [Why Elon Musk's DOGE is amassing sensitive government data - The Washington Post](https://www.washingtonpost.com/business/2025/05/07/doge-government-data-immigration-social-security)
    > 💬 *", Lisa Rein and Rachel Siegel The U.S. DOGE Service is racing to build a single centralized database with vast troves of personal information about millions of U.S. citizens and residents, a campaign that often violates or disregards core privacy and security protections meant to keep such information safe, government workers say. pixel [...] Democracy Dies in Darkness # DOGE aims to pool federal ..."*
  - `[DuckDuckGo]` [2026 FBI data breach - Wikipedia](https://en.wikipedia.org/wiki/2026_FBI_data_breach)
    > 💬 *"The 2026 FBI data breach was a cyberattack on the Federal Bureau of Investigation 's recruitment portal, FBIJobs.gov, in September 2026, in which the extortion group ShinyHunters claimed to have stolen personal data on nearly all current and former FBI employees and job applicants. [1][2] The FBI designated the matter a cybersecurity incident on September 22, 2026, [3] and later attributed the ..."*

---

## <span class="badge-tuttu">TUTTU</span> | AI Fikirlerimizi Manipüle Edebilir Mi? - S.A.H E123 | 📅 2025-05-04
### 1. Utku, yapay zekanın fotoğraftan konum bulma (Geoguessr) ve görsel akıl yürütmede insanla olan rekabetinin 5-10 yıl sürmeyeceğini, en fazla 6 ay içinde yapay zekanın arayı inanılmaz açarak bu rekabeti tamamen bitireceğini söylüyor.
- **Sonuç:** <span class="badge-tuttu">TUTTU</span> (Güven Skoru: **5.1/10**)
- **Olasılık Dağılımı:** `TUTMADI: %7.0 | KISMEN TUTTU: %29.0 | TUTTU: %50.9 | BELIRSIZ: %13.0`
- **Videoda Ne Demişti:** ChatGPT'nin profesyonel bir Geoguessr oyuncusunu yenmesi haberini yorumlayan Utku Şen, satrançtaki Kasparov ve Deep Blue sürecini hatırlatıyor. Bilgisayarın insanı geçtikten sonra arayı açmasının bu sefer yıllar değil sadece birkaç ay alacağını, 6 ay sonra bu rekabetin tamamen biteceğini kendi tahmini olarak ekliyor.
- **İncelenen Web Kanıtları:**
  - `[Tavily]` [GeoGuessr AI - Use AI to Find Where Any Street View Was Taken | GeoAxis](https://geoaxis.ai/geoguessr-ai)
    > 💬 *"## FAQ - GeoGuessr AI ### Is there an AI that plays GeoGuessr? Yes - several, but they vary in accuracy. GeoAxis is the public-benchmark leader on street-level imagery, so “the AI for GeoGuessr” is functionally what GeoAxis is. ### Can AI beat top human GeoGuessr players? On unfamiliar regions and across a long round set, yes. Top human players still win on familiar regions and on rounds with rare..."*
  - `[Tavily]` [GeoGuessr AI: How PIGEON Beat a Pro, and Is It Cheating?](https://geospys.com/blog/geoguessr-ai)
    > 💬 *"Short answer The best GeoGuessr AI already outplays almost every human player. Stanford’s PIGEON model ranked in the top 0.01% of players in a blind experiment and won six out of six games against professional Trevor Rainbolt. Using AI for help during play is cheating under GeoGuessr’s rules, reviewing finished rounds with it is a fair way to learn. [...] The live test is what made it more than a ..."*
  - `[Tavily]` [Sony's AI robot is beating the best human ping pong players](https://finance.yahoo.com/video/sonys-ai-robot-beating-best-103000301.html)
    > 💬 *"1. Deirdre Bosa Live! Deirdre Bosa Live! 2. AI Trending FAA grounds flights Stock market today Live: Nvidia updates Social Security cuts: 28 states could lose $500 or more per month Yahoo Finance Video # Sony's AI robot is beating the best human ping pong players Yahoo Finance Video Yahoo Finance Video 6758.T Sony (SONY) has built a "ping pong robot" that uses agentic artificial intelligence (AI) ..."*
  - `[Tavily]` [Sony's AI robot is beating the best human ping pong players](https://ca.finance.yahoo.com/video/sonys-ai-robot-beating-best-103000301.html)
    > 💬 *"Yahoo Finance Video # Sony's AI robot is beating the best human ping pong players Yahoo Finance Video Yahoo Finance Video 6758.T Sony (SONY) has built a "ping pong robot" that uses agentic artificial intelligence (AI) to beat expert human players. Yahoo Finance Tech Editor Dan Howley explains more. Terms and Privacy Policy Privacy Dashboard ## Recommended Stories [...] Oops, something went wrong S..."*
  - `[DuckDuckGo]` [GitHub - Nutlope/geoguessbench: An open GeoGuessr benchmark ...](https://github.com/Nutlope/geoguessbench)
    > 💬 *"Oct 6, 2026 · An open GeoGuessr benchmark for AI models. Contribute to Nutlope/geoguessbench development by creating an account on GitHub."*

---

## <span class="badge-kismen">KISMEN TUTTU</span> | AI Fikirlerimizi Manipüle Edebilir Mi? - S.A.H E123 | 📅 2025-05-04
### 2. Utku, yapay zeka botlarıyla insanları ikna etmenin maliyetsiz hale gelmesiyle birlikte ileride büyük platform sahiplerinin devletlere gizlice bot ordusu servisi satacağını ve bu sistemlerin kitle manipülasyonunda mutlaka kullanılacağını söylüyor.
- **Sonuç:** <span class="badge-kismen">KISMEN TUTTU</span> (Güven Skoru: **4.1/10**)
- **Olasılık Dağılımı:** `TUTTU: %30.4 | BELIRSIZ: %25.6 | TUTMADI: %3.0 | KISMEN TUTTU: %41.0`
- **Videoda Ne Demişti:** Zürih Üniversitesi'nin yapay zeka botlarının insan fikirlerini değiştirmede 6 kat daha başarılı olduğunu gösteren araştırmasını değerlendiren Utku Şen, bot maliyetlerinin çok düşmesine dikkat çekiyor. İleride Elon Musk gibi platform sahiplerinin devletlere el altından bot servisi satacağını ve bu gücün algı operasyonlarında kesinlikle kullanılacağını kendi tezi olarak anlatıyor.
- **İncelenen Web Kanıtları:**
  - `[Tavily]` [The Second AI Election: Testing the Safeguards Before November | Brennan Center for Justice](https://www.brennancenter.org/our-work/analysis-opinion/second-ai-election-testing-safeguards-november)
    > 💬 *"battlefield by foreign nations. Chinese actors have been credibly accused of standing up at least 5,000 inauthentic X accounts controlled by an AI large language model system, according to recentreports. This operation, nicknamed “Green Cicada,” was deployed to influence political narratives and sow discord in the United States and other countries. Even more recently, new reporting alleges that Ru..."*
  - `[Tavily]` [How AI chatbots can mislead with election advice : NPR](https://www.npr.org/2026/11/02/nx-s1-6025407/chatbots-midterms-voting-advice)
    > 💬 *"Meta, Anthropic, OpenAI and Google said they are working to prevent their chatbots from producing disinformation about the elections, such as incorrect information about poll site locations and opening times or misleading deepfake images, consistent with longstanding industry efforts that began after Russia's influence campaign during the 2016 elections. ### Americans increasingly use chatbots for..."*
  - `[Tavily]` [Chatbots and deepfakes in the 2026 midterms: An evidence-based AI guide for journalists - SciLine](https://www.sciline.org/elections/ai-artificial-intelligence-chatbots)
    > 💬 *"2016 and 2020, the authors found. The bots trained to shift opinion in Trump’s favor moved voters 1.5 points in that direction for likely Harris voters. Across all three countries, the AI models nudging participants on the right made less accurate claims. [...] “The chatbots we tested resisted election misinformation because accurate, well-sourced information was easy to find online,” writes Lawre..."*
  - `[Tavily]` [A.I. and Its Dangers Are Embedded In the Midterm Elections - The New York Times](https://www.nytimes.com/2026/10/22/business/media/ai-disinfo-chatbots-elections.html)
    > 💬 *"A.I. tools, some introduced just months before the election, have contributed to biased and inaccurate information about the polls and amplified foreign influence operations. They have also elevated low-quality slop content, which is now tainting the training data that informs chatbot responses, according to researchers. [...] Ahead of the midterms next month, chatbots, media generation services a..."*
  - `[DuckDuckGo]` [UNMASKING THE THREAT: How Automated Bot Networks Manipulate ...](https://www.humansecurity.com/learn/resources/how-automated-bot-networks-manipulate-elections-globally/)
    > 💬 *"Early uses were relatively benign, but recent advancements have enabled complex disinformation campaigns and direct attacks on electoral systems. The 2016 U.S. presidential election marked a pivotal moment, showcasing the power of state-sponsored bots in shaping political discourse."*

---

