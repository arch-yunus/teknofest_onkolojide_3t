# ONKOLOJİDE 3T YARIŞMASI YARI FİNAL PROJE RAPORU

**PROJE ADI:** GlioSight — Multimodal MRI & Biotech AI Platform
**TAKIM ADI:** [Takım Adınızı Buraya Giriniz]
**BAŞVURU ID:** [Başvuru ID Giriniz]
**TAKIM ID:** [Takım ID Giriniz]

---

## BİYOTEKNOLOJİ ALANI
Projemiz "GlioSight", doğrudan **Beyin Kanseri (Glioblastoma)** üzerine odaklanan tam kapsamlı bir Karar Destek Sistemidir. Şartname kapsamında; Yapay Zeka Destekli Yeni Nesil İlaç Geliştirme (moleküler docking ve bağlama afinitesi), Terapötik Kanser Aşıları (neoantijen tahmini) ve Hücresel/Moleküler Patoloji (WHO CNS 5 standartlarında IDH, MGMT, 1p/19q genetik ve epigenetik biyobelirteç tahmini) gibi konuları doğrudan içermektedir.

## PROJE ÖZETİ
GlioSight, TEKNOFEST Onkolojide 3T yarışması kapsamında beyin kanseri (glioblastoma) teşhis ve tedavi süreçlerini otonomlaştıran, multimodal MRI ve biyoteknolojik verileri entegre eden "Egemen Katman" (Sovereignty Tier) bir yapay zeka ekosistemidir. Çalışmanın amacı; radyolojik, patolojik ve klinik verileri tek bir merkezde toplayarak yüksek doğrulukla 3B tümör segmentasyonu, radyomik analiz, moleküler biyobelirteç tahmini ve kişiselleştirilmiş ilaç/aşı tasarımı sağlamaktır. Bu yaklaşım, hekimlerin klinik iş yükünü hafifletirken, tedavi süreçlerinde veri destekli optimum kararların alınmasını mümkün kılar.

## SORUN TANIMI
Beyin kanseri tedavisinde en büyük zorluklardan biri, tümörün oldukça heterojen bir yapıya sahip olması ve tedavi sürecinin (tanı, cerrahi planlama, radyoterapi, kemoterapi) birbirinden bağımsız birçok farklı disipline dağılmış olmasıdır. Mevcut yazılımlar ya sadece görüntüleme (segmentasyon) üzerine ya da sadece genetik üzerine çalışmaktadır. Bu durum tedavi planlamasında gecikmelere, hekimler arası multidisipliner iletişim eksikliğine ve hastaya özgü yeni nesil ilaç/aşı geliştirme aşamalarında zaman kaybına yol açmaktadır. GlioSight, bu parçalı ve karmaşık yapıyı ortadan kaldırarak beyin kanseri tedavisindeki tüm süreçleri tek bir platform altında bütünleştirmeyi hedefler.

## ÇÖZÜM
Projemiz, belirtilen sorunları aşmak için yarışma kapsamındaki 12 farklı medikal onkoloji alt disiplinini tek bir "Sovereignty Engine" altında birleştirir. Çok modlu (T1, T1Gd, T2, FLAIR) MR görüntüleri kullanılarak tümör alt bölgeleri (nekroz, ödem, gelişen tümör) yapay zeka ile otomatik olarak belirlenir. Sağkalım analizi (Survival Analysis) ve RANO kriterlerine göre tedavi yanıtı takibi (CR, PR, SD, PD) sayısal verilere dökülür. Biyoteknoloji modülümüz ise, hastanın moleküler profiline uygun ilaç bağlanma simülasyonları gerçekleştirerek kişiselleştirilmiş tedavi ve terapötik aşı dizilim önerileri sunar.

## YÖNTEM
Önerilen çözümde Derin Öğrenme (Deep Learning) ve Radyogenomik prensipleri kullanılmaktadır. Görüntü işleme aşamasında PyTorch ve MONAI tabanlı 3D U-Net mimarileri tercih edilmiş olup, XAI (Açıklanabilir Yapay Zeka - Grad-CAM) özellikleri sayesinde hekimlerin modelin kararlarını izleyebilmesi sağlanmıştır. Moleküler patoloji aşamasında WHO CNS 5 kriterlerine tam uyumlu IDH ve MGMT mutasyon sınıflandırma algoritmaları çalıştırılır. Modeller BraTS gibi uluslararası standartlardaki verisetleri ile eğitilmiştir. Hekimlerin kolayca erişebilmesi için geliştirilen prototip (dashboard) arayüzü, arka planda API servisleri üzerinden gerçek zamanlı çıkarım (inference) yapmaktadır.

## YENİLİKÇİ YÖNÜ VE ÖZGÜN DEĞERİ
Projemizin piyasadaki mevcut ürünlerden ve literatürdeki benzer çalışmalardan en büyük farkı; yalnızca tanı odaklı bir segmentasyon yazılımı olmamasıdır. GlioSight, Dijital Patoloji Emülasyonu, 3B Cerrahi Navigasyon Uyarıları, İlaç Keşfi (Docking) ve giyilebilir cihazlarla entegre ağrı yönetimi (Algoloji) süreçlerini eş zamanlı sunan dünyadaki nadir ekosistem tasarımlarından biridir. Bu bütüncül yaklaşım ve yüksek uyumluluk standartları, projenin özgün değerini oluşturmaktadır.

## TEKNOLOJİ HAZIRLIK SEVİYESİ (THS)
Projeye THS 3 (Analitik ve Deneysel Kritik İşlev Doğrulaması) seviyesinde başlanmış olup, proje sonunda laboratuvar ortamında yapay zeka ve yazılım prototipinin validasyonları tamamlanarak THS 4 ve aşamalı olarak THS 5 (Laboratuvar ve klinik simülasyon ortamında doğrulama) seviyesine erişilmesi planlanmaktadır. Şu aşamada temel algoritmaların tezgâh üstü doğrulama süreçleri yapılmış ve arayüz entegrasyonu tamamlanmıştır.

## UYGULANABİLİRLİK
GlioSight projesi, mevcut hastane altyapılarına (HBYS ve PACS) kolayca entegre olabilen RESTful API tabanlı modüler bir mimari ile kodlanmıştır. İhtiyaca göre bulut tabanlı veya tamamen izole hastane içi sunucularda (on-premise) çalıştırılabileceğinden veri gizliliği kurallarına uyumludur. Geliştirilen Streamlit tabanlı kullanıcı arayüzü sayesinde donanım bağımsız ticari bir SaaS medikal yazılım ürününe kolayca dönüştürülebilir.

## TAHMİNİ MALİYET VE PROJE ZAMAN PLANLAMASI
Sistem tamamen yazılım tabanlı bir karar destek platformu olduğundan, piyasadaki donanım tabanlı büyük tıbbi cihazlara kıyasla yatırım maliyeti oldukça düşüktür. 
**Zaman Planlaması:**
- **1. Ay:** Veri ön işleme, temizleme ve standardizasyon süreçleri.
- **2. Ay:** 3D Model eğitimleri (Segmentasyon) ve Radyogenomik algoritmaların optimizasyonu.
- **3. Ay:** Biyoteknolojik simülasyon modüllerinin (İlaç ve Aşı tahmini) entegrasyonu.
- **4. Ay:** Hekim arayüzü prototipinin testleri, klinik uzman görüşlerinin alınması ve validasyon süreçleri.
**Maliyetler:** Temel maliyet kalemi, yapay zeka modellerinin eğitimi ve sunucu barındırma için gereken GPU işlem gücü masraflarından oluşmaktadır.

## PROJENİN HEDEF KİTLESİ
Projenin temel kullanıcı kitlesi; radyologlar, beyin ve sinir cerrahları, medikal onkologlar ile onkolojik ilaç/aşı araştırmaları yürüten biyoteknoloji laboratuvarlarıdır. Son faydalanıcı kitle ise, daha hızlı tanı alarak kişiselleştirilmiş ve doğru tedavi planlarına kavuşan beyin kanseri hastalarıdır.

## RİSKLER
**Olası Risk:** Yapay zeka modellerinin, veriseti dışındaki farklı cihazlardan gelen veya gürültülü MR görüntülerinde performans kaybı yaşaması (domain shift).
**Çözüm Planı (B Planı):** Sistemin genelleştirme yeteneğini artırmak için veri artırma (data augmentation) yöntemlerinin çeşitlendirilmesi ve transfer öğrenme (transfer learning) mimarilerinin kullanılarak modellerin farklı merkezlerdeki verilere uyarlanması planlanmaktadır.

## KAYNAKLAR
1. Menze, B. H., et al. (2015). "The Multimodal Brain Tumor Image Segmentation Benchmark (BRATS)". IEEE Transactions on Medical Imaging.
2. Louis, D. N., et al. (2021). "The 2021 WHO Classification of Tumors of the Central Nervous System: a summary". Neuro-oncology.
3. Keras & PyTorch Documentation on 3D Medical Imaging.
4. MONAI (Medical Open Network for AI) Framework Dokümantasyonu (2024). (Erişim Tarihi: Ekim 2025)
