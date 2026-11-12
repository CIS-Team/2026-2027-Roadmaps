# Cyber Security Learning Map

Understand the systems beneath the surface, then explore how applications fail and how programs behave.

This map connects three learning paths: **Cybersecurity Entry**, **Web Security & Penetration Testing**, and **Malware Analysis**. Use it to find your starting point and open the detailed roadmap for its resources, labs, and tasks.

## The big picture

```mermaid
flowchart TD
    START["CYBER SECURITY"] --> FOUND["BUILD YOUR FOUNDATIONS"]
    FOUND --> N["Network fundamentals"]
    N --> L["Linux essentials"]
    L --> P["Python programming"]
    P --> S["Security+ fundamentals"]
    S --> C["Cryptography"]
    C --> CHOOSE{"Choose a direction"}

    CHOOSE --> WEB["WEB SECURITY"]
    WEB --> W1["Web development fundamentals"]
    W1 --> W2["Web security fundamentals"]
    W2 --> W3["Advanced web vulnerabilities"]
    W3 --> W4["Common web vulnerabilities & reporting"]

    CHOOSE --> MAL["MALWARE ANALYSIS"]
    MAL --> M1["C programming"]
    M1 --> M2["Assembly"]
    M2 --> M3["Intel microprocessor & operating systems"]
    M3 --> M4["Fundamentals of malware analysis"]
    M4 --> M5["Fundamentals of reverse engineering"]
    M5 --> M6["Deep dive in reverse engineering"]
    M6 --> M7["Deep dive in malware analysis"]

    classDef root fill:#0f172a,stroke:#64748b,color:#ffffff
    classDef foundation fill:#e0f2fe,stroke:#0284c7,color:#0c4a6e
    classDef web fill:#ede9fe,stroke:#7c3aed,color:#4c1d95
    classDef malware fill:#fef3c7,stroke:#d97706,color:#78350f
    class START,CHOOSE root
    class FOUND,N,L,P,S,C foundation
    class WEB,W1,W2,W3,W4 web
    class MAL,M1,M2,M3,M4,M5,M6,M7 malware
```

*The branches show different areas to explore, not a requirement to complete both. If you already know the foundations, start with the path that fits your background.*

---

## 01 · Foundations

Build familiarity with networks, operating systems, programming, and core security concepts.

| Sequence | Focus |
| :---: | --- |
| 1 | Network fundamentals |
| 2 | Linux essentials |
| 3 | Python programming |
| 4 | Security+ fundamentals |
| 5 | Cryptography |

**[Open the Cybersecurity Entry roadmap →](cyber-entry-roadmap.md)**

## 02 · Choose your specialization

### Web Security & Penetration Testing

Explore web technologies, vulnerability classes, practical labs, and reporting through a **16-week learning path**.

| Stage | Focus |
| --- | --- |
| **Month 1** | Web Development Fundamentals |
| **Month 2** | Web Security Fundamentals |
| **Month 3** | Advanced Web Vulnerabilities |
| **Month 4** | Common Web Vulnerabilities and Reporting |

The detailed roadmap includes weekly resources, PortSwigger labs, TryHackMe rooms, and tasks.

**[Open the Web Security roadmap →](penetration-testing-roadmap.md)**

### Malware Analysis

Study program behavior through programming, low-level systems, reverse engineering, and malware analysis.

| Sequence | Focus |
| :---: | --- |
| 1 | C programming |
| 2 | Assembly |
| 3 | Intel microprocessor & operating systems |
| 4 | Fundamentals of malware analysis |
| 5 | Fundamentals of reverse engineering |
| 6 | Deep dive in reverse engineering |
| 7 | Deep dive in malware analysis |

The detailed roadmap includes courses, books, and additional reference resources.

**[Open the Malware Analysis roadmap →](malware-analysis-roadmap.md)**

---

## How to use the map

**Locate your starting point → Open the detailed roadmap → Learn and practice → Revisit what needs work**

Follow the sequence inside your chosen roadmap. Use its resources and activities, keep notes on what you discover, and return to the foundations whenever you need them.

[← All learning tracks](../README.md)
