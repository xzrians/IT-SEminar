# 📊 10: Visual Plan & Master Flow Diagrams

Dokumen ini menyediakan gambaran visual lengkap bagi **NextGen Tech Summit** merangkumi aliran masa, tiang pembelajaran, dan struktur operasi.

---

## 1. Master Event Flow & Timeline (08:30 – 12:00)

```mermaid
flowchart TD
    subgraph S1 ["Phase 1: Arrival & Energize (08:30 – 09:15)"]
        A["08:30 – 09:00 AM<br/>Check-in & Team Sorting<br/><i>(Badges, Table assignment, Lofi/Synthwave)</i>"] --> B["09:00 – 09:15 AM<br/>Dynamic Kickoff & Ice Breaker<br/><i>(Tech Charades & Emoji Decoder)</i>"]
    end

    subgraph S2 ["Phase 2: Tech & AI Exploration (09:15 – 10:00)"]
        B --> C["09:15 – 09:35 AM<br/>Tech Talk: Technology Around Us<br/><i>(GenAI, LLMs, Algorithms, Future Careers)</i>"]
        C --> D["09:35 – 10:00 AM<br/>Fast-Answer Tech Showdown<br/><i>(5 Soalan Pantas: Siapa Cepat, Dia Menang - Tanpa Telefon)</i>"]
    end

    subgraph S3 ["Phase 3: Recharge & Digital Resilience (10:00 – 10:45)"]
        D --> E["10:00 – 10:15 AM<br/>Networking & Refreshment Break 🥐<br/><i>(Snacks & informal mentor chats)</i>"]
        E --> F["10:15 – 10:45 AM<br/>Interactive Workshop: Be Smart Online<br/><i>(Scams, Phishing, Deepfakes, 2FA, Digital Footprints)</i>"]
    end

    subgraph S4 ["Phase 4: Innovation Sprint & Pitches (10:45 – 11:50)"]
        F --> G["10:45 – 11:30 AM (45 min)<br/>Hands-On Startup Sprint: The AI Pitch Challenge<br/><i>(Problem validation, Mahjong canvas poster creation)</i>"]
        G --> H["11:30 – 11:50 AM (20 min)<br/>Startup Pitch Showcase & Judging<br/><i>(Rapid-fire 2-3 min pitches per team)</i>"]
    end

    subgraph S5 ["Phase 5: Recognition & Closing (11:50 – 12:00)"]
        H --> I["11:50 – 12:00 PM<br/>Grand Awards & Photo Session 📸<br/><i>(Quiz Champs, Pitch Winners, ASDAF Frame)</i>"]
    end

    style S1 fill:#f0f4ff,stroke:#4a6fa5,stroke-width:2px
    style S2 fill:#e8f8f5,stroke:#2ec4b6,stroke-width:2px
    style S3 fill:#fff8e7,stroke:#ffb703,stroke-width:2px
    style S4 fill:#fdf0ed,stroke:#e76f51,stroke-width:2px
    style S5 fill:#f3e8ff,stroke:#9d4edd,stroke-width:2px
```

---

## 2. Core Pillars & Participant Learning Journey

```mermaid
graph LR
    subgraph P1 ["1. AI & Algorithms"]
        P1A["Real-World GenAI<br/><i>(ChatGPT, Claude, Midjourney)</i>"]
        P1B["Recommendation Engines<br/><i>(TikTok, Reels, YouTube)</i>"]
    end

    subgraph P2 ["2. Cyber Resilience"]
        P2A["Social Engineering Defense<br/><i>(Phishing, Account Hijacking)</i>"]
        P2B["Reputation & Privacy<br/><i>(Deepfakes, 2FA, Digital Footprint)</i>"]
    end

    subgraph P3 ["3. Startup Sprint"]
        P3A["Lean Mahjong Poster<br/><i>(Problem, AI Feature, User Impact)</i>"]
        P3B["3-Minute Live Pitch<br/><i>(Public speaking & collegiate Q&A)</i>"]
    end

    subgraph P4 ["4. Inclusive Mentorship"]
        P4A["Mixed-Gender Table Dynamics<br/><i>(Equal leadership & role division)</i>"]
        P4B["Targeted Support<br/><i>(Form 1–5 & PPKI inclusivity)</i>"]
    end

    P1 --> P3
    P2 --> P3
    P4 -.-> P1
    P4 -.-> P2
    P4 -.-> P3
```

---

## 3. Operational Structure & Stakeholder Alignment

```mermaid
flowchart TD
    subgraph Leadership ["Central Committee & Leads"]
        DIR["Program Director / Emcee<br/><i>(Run of show, timing, stage flow)</i>"]
        TECH["Technical & AV Lead<br/><i>(Projector, Quiz Slides, Audio/Mic, Timer)</i>"]
        LOG["Logistics & Refreshments Lead<br/><i>(Kits, Mahjong sets, Food & Medals)</i>"]
    end

    subgraph Floor ["Floor Mentorship (7 Tables / 47 ASDAF Students)"]
        F1["Mentor Team 1–3<br/><i>(Tables 1 to 3: Lower Secondary)</i>"]
        F2["Mentor Team 4–6<br/><i>(Tables 4 to 6: Upper Secondary)</i>"]
        F3["Mentor Table 7<br/><i>(Table 7: Inclusive / PPKI Buddy Support)</i>"]
    end

    subgraph StageFlow ["Stage & Review Panel"]
        JUDGE["Judging Panel<br/><i>(Best Innovation, Best Model, Best Delivery)</i>"]
        ASDAF["ASDAF Partner Representatives<br/><i>(Appreciation frame & certificates)</i>"]
    end

    Leadership --> Floor
    Floor --> StageFlow
```
