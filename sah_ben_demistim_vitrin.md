# Tutan Öngörüler (Vitrin)

Utku Şen'in S.A.H yayınlarında önceden haber verip haklı çıktığı tahminler.

> **Genel Durum:** 🟢 Tuttu: **1** | 🟡 Kısmen Tuttu: **1** | 🔴 Tutmadı: **2** | ⚪ Belirsiz: **2**

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

