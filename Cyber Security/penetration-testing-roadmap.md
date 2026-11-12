# Web Security Roadmap

A 16-week learning path from web development fundamentals to common and advanced web vulnerabilities, ending with penetration testing reports.

## Table of Contents

- [Roadmap Overview](#roadmap-overview)
- [Learning Objectives](#learning-objectives)
- [Learning Journey](#learning-journey)
  - [Month 1: Web Development Fundamentals](#month-1-web-development-fundamentals)
  - [Month 2: Web Security Fundamentals](#month-2-web-security-fundamentals)
  - [Month 3: Advanced Web Vulnerabilities](#month-3-advanced-web-vulnerabilities)
  - [Month 4: Common Web Vulnerabilities and Reporting](#month-4-common-web-vulnerabilities-and-reporting)
- [Weekly Tasks and Deliverables](#weekly-tasks-and-deliverables)
  - [Month 1 Tasks](#month-1-tasks)
  - [Month 2 Tasks](#month-2-tasks)
  - [Month 3 Tasks](#month-3-tasks)
  - [Month 4 Tasks](#month-4-tasks)
- [Final Learning Outcomes](#final-learning-outcomes)

## Roadmap Overview

| | |
|---|---|
| **Duration** | 4 Months |
| **Structure** | 4 Weeks per Month |
| **Total labs** | 86 |
| **Total learning hours** | Not specified in the source roadmap |
| **Prerequisites** | Not specified in the source roadmap |

> Lab total as stated in the source roadmap.

| Month | Focus | Weeks |
|---|---|---|
| 1 | Web Development Fundamentals | HTML · JavaScript · SQL · PHP |
| 2 | Web Security Fundamentals | Security Tools and Web Technologies · Reconnaissance · Broken Access Control and IDOR · Information Disclosure and CORS |
| 3 | Advanced Web Vulnerabilities | Path Traversal and File Upload · Authentication and JWT · OAuth and Business Logic Vulnerabilities · CSRF and SSRF |
| 4 | Common Web Vulnerabilities and Reporting | SQL Injection · Cross-Site Scripting (XSS) · XXE and SSTI · OS Command Injection, Host Header Injection, and Reporting |

## Learning Objectives

- Web development fundamentals: HTML, JavaScript, SQL and PHP.
- Web security fundamentals: Burp Suite, Nmap, Hydra, web technologies, reconnaissance, Broken Access Control, IDOR, Information Disclosure and CORS.
- Advanced web vulnerabilities: Path Traversal, File Upload, Authentication, JWT, OAuth, Business Logic, CSRF and SSRF.
- Common web vulnerabilities and reporting: SQL Injection, XSS, XXE, SSTI, OS Command Injection, Host Header Injection and Penetration Testing Reports.

## Learning Journey

### Month 1: Web Development Fundamentals

#### Week 1: HTML

**Resources**

1. [HTML course playlist](https://www.youtube.com/watch?v=Dv39fDYei9A&list=PLknwEmKsW8OtLRQPTLms79499meY2D6ij)

#### Week 2: JavaScript

**Resources**

1. [JavaScript course playlist](https://www.youtube.com/playlist?list=PLknwEmKsW8OuTqUDaFRBiAViDZ5uI3VcE)

#### Week 3: SQL

**Resources**

1. [SQL course playlist](https://www.youtube.com/playlist?list=PLDRMxi70CdSAhaQZzkR1uyNsMOezEChMA)

#### Week 4: PHP

**Resources**

1. [PHP course video](https://www.youtube.com/watch?v=qmvjwRbtNww)

### Month 2: Web Security Fundamentals

> **Note:** Tools may require up to 3 additional days if needed.

#### Week 1: Security Tools and Web Technologies

**Topics**

- Burp Suite
- Nmap
- Hydra
- Web Technologies

**Resources**

1. [Burp Suite](https://www.youtube.com/playlist?list=PLDRMxi70CdSBzjCKsC0clrioNmlAPvASK)
2. [Nmap](https://www.youtube.com/playlist?list=PLgCu8TiZE3Oba_FDgrWxaHemCCI5rOza7)
3. [Hydra](https://youtu.be/4q1l-5rQ4rQ?si=tXl_A7UjLu180IET)
4. [Web Technologies](https://www.youtube.com/watch?v=n8Gx4dYJFG4&list=PLsB1gqjeUAh_99a9LbVbxg-nBV79o0kW3&index=2)

**TryHackMe rooms**

- [Hydra](https://tryhackme.com/room/hydra)
- [Further Nmap](https://tryhackme.com/room/furthernmap)

#### Week 2: Reconnaissance

**Resources**

1. [Reconnaissance playlist](https://www.youtube.com/playlist?list=PLEHdb4yX2v-3aS3aFGpVBJawx9C3aZeZj)

#### Week 3: Broken Access Control and IDOR

##### Broken Access Control

**Resources**

1. [Broken Access Control video](https://www.youtube.com/watch?v=8gLOhMrIpVo&list=PLTSGZiCtCBfMMLkmaN7tGEhbc0QbOEtEA&index=)

**PortSwigger labs**

| # | Lab | Level |
|---|---|---|
| 1 | Unprotected admin functionality | Apprentice |
| 2 | Unprotected admin functionality with unpredictable URL | Apprentice |
| 3 | User role controlled by request parameter | Apprentice |
| 4 | User role can be modified in user profile | Apprentice |

##### IDOR – Insecure Direct Object References

**Resources**

1. [IDOR video](https://www.youtube.com/watch?v=BfbS8uRjeAg)

**TryHackMe rooms**

- [IDOR](https://tryhackme.com/room/idor-aoc2025-zl6MywQid9)

**PortSwigger labs**

| # | Lab | Level |
|---|---|---|
| 1 | User ID controlled by request parameter | Apprentice |
| 2 | User ID controlled by request parameter, with unpredictable user IDs | Apprentice |
| 3 | User ID controlled by request parameter with data leakage in redirect | Apprentice |
| 4 | User ID controlled by request parameter with password disclosure | Apprentice |
| 5 | Insecure direct object references | Apprentice |

#### Week 4: Information Disclosure and CORS

##### Information Disclosure

**Resources**

1. [Video 1](https://youtu.be/Jzp9xuha-jQ?si=Dcwd5-TFU-oaXknD)
2. [Video 2](https://youtu.be/V9Bc_Addfps?si=NVtMxRX_8MdZDp6d)

**PortSwigger labs**

| # | Lab | Level |
|---|---|---|
| 1 | Information disclosure in error messages | Apprentice |
| 2 | Information disclosure on debug page | Apprentice |
| 3 | Source code disclosure via backup files | Apprentice |
| 4 | Authentication bypass via information disclosure | Apprentice |

##### Cross-Origin Resource Sharing (CORS)

**Resources**

1. [CORS video](https://youtu.be/OcrmPMSjdSw?si=UJuhsfQV9WSyTKYU)

**PortSwigger labs**

| # | Lab | Level |
|---|---|---|
| 1 | CORS vulnerability with basic origin reflection | Apprentice |
| 2 | CORS vulnerability with trusted null origin | Apprentice |
| 3 | CORS vulnerability with trusted insecure protocols22 | Practitioner |

### Month 3: Advanced Web Vulnerabilities

#### Week 1: Path Traversal and File Upload

##### Path Traversal

**Resources**

1. [Video 1](https://youtu.be/YS7I1_xMCGc?si=n-vP18uCa7TFA8rX)
2. [Video 2](https://youtu.be/KVbyVDk5O7E?si=RdNbgg_qrUWFdDyS)

**PortSwigger labs**

| # | Lab | Level |
|---|---|---|
| 1 | File path traversal, simple case | Apprentice |
| 2 | File path traversal, traversal sequences blocked with absolute path bypass | Practitioner |
| 3 | File path traversal, traversal sequences stripped non-recursively | Practitioner |
| 4 | File path traversal, traversal sequences stripped with superfluous URL-decode | Practitioner |
| 5 | File path traversal, validation of start of path | Practitioner |

##### File Upload

**Resources**

1. [File Upload video](https://youtu.be/E9yyhxzxeok?si=B4icUGofN_K6od8i)

**PortSwigger labs**

| # | Lab | Level |
|---|---|---|
| 1 | Remote code execution via web shell upload | Apprentice |
| 2 | Web shell upload via Content-Type restriction bypass | Apprentice |
| 3 | Web shell upload via path traversal | Practitioner |

#### Week 2: Authentication and JWT

##### Authentication

**Resources**

1. [Video 1](https://www.youtube.com/watch?v=afASRDvimwg&list=PLsB1gqjeUAh_99a9LbVbxg-nBV79o0kW3&index=6)
2. [Video 2](https://www.youtube.com/watch?v=HfA5CKjGwU8)

**PortSwigger labs**

| # | Lab | Level |
|---|---|---|
| 1 | Username enumeration via different responses | Apprentice |
| 2 | 2FA simple bypass | Apprentice |
| 3 | Password reset broken logic | Apprentice |
| 4 | Username enumeration via subtly different responses | Practitioner |
| 5 | Username enumeration via response timing | Practitioner |
| 6 | Broken brute-force protection, IP block | Practitioner |
| 7 | Additional LAB (name not provided in the original list) | Practitioner |

##### JSON Web Tokens (JWT)

**Resources**

1. [Video 1](https://www.youtube.com/watch?v=DDqfdH-2ULI)
2. [Video 2](https://youtu.be/2pZnezSBO3k?si=InS9VRP1EI3evweP)

**PortSwigger labs**

| # | Lab | Level |
|---|---|---|
| 1 | JWT authentication bypass via unverified signature | Apprentice |
| 2 | JWT authentication bypass via flawed signature verification | Apprentice |
| 3 | JWT authentication bypass via weak signing key | Practitioner |
| 4 | JWT authentication bypass via jwk header injection | Practitioner |
| 5 | JWT authentication bypass via jku header injection | Practitioner |

#### Week 3: OAuth and Business Logic Vulnerabilities

##### OAuth

**Resources**

1. [OAuth video](https://www.youtube.com/watch?v=1PLdUpHbcXE&list=PLsB1gqjeUAh_99a9LbVbxg-nBV79o0kW3&index=15)

**PortSwigger labs**

| # | Lab | Level |
|---|---|---|
| 1 | Authentication bypass via OAuth implicit flow | Apprentice |
| 2 | SSRF via OpenID dynamic client registration | Practitioner |
| 3 | Forced OAuth profile linking | Practitioner |

##### Business Logic Vulnerabilities

**Resources**

1. [Video 1](https://youtu.be/IaUl6g82C1Q?si=RXQ_0UWF3YsIcaWH)
2. [Video 2](https://www.youtube.com/playlist?list=PLuyTk2_mYISIbsZEVy7aZmlW2qEhCfWpq)

**PortSwigger labs**

| # | Lab | Level |
|---|---|---|
| 1 | Excessive trust in client-side controls | Apprentice |
| 2 | High-level logic vulnerability | Apprentice |
| 3 | Inconsistent security controls | Apprentice |
| 4 | Flawed enforcement of business rules | Apprentice |
| 5 | Low-level logic flaw | Practitioner |
| 6 | Inconsistent handling of exceptional input | Practitioner |
| 7 | Weak isolation on dual-use endpoint | Practitioner |
| 8 | Insufficient workflow validation | Practitioner |

#### Week 4: CSRF and SSRF

##### Cross-Site Request Forgery (CSRF)

**Resources**

1. [Video 1](https://www.youtube.com/watch?v=n8Gx4dYJFG4&list=PLsB1gqjeUAh_99a9LbVbxg-nBV79o0kW3)
2. [Video 2](https://www.youtube.com/watch?v=NZMAqk6sZHE&list=PLsB1gqjeUAh_99a9LbVbxg-nBV79o0kW3&index=5)

**TryHackMe rooms**

- [CSRF Introduction](https://tryhackme.com/room/csrfintroduction)

**PortSwigger labs**

| # | Lab | Level | Status |
|---|---|---|---|
| 1 | CSRF vulnerability with no defenses | Apprentice | Not Solved |
| 2 | CSRF where token validation depends on request method | Practitioner | Not Solved |
| 3 | CSRF where token validation depends on token being present | Practitioner | Not Solved |
| 4 | CSRF where token is not tied to user session | Practitioner | Not Solved |

##### Server-Side Request Forgery (SSRF)

**Resources**

1. [SSRF video](https://www.youtube.com/watch?v=g7RKLpnxLM8&list=PLsB1gqjeUAh_99a9LbVbxg-nBV79o0kW3&index=31)

**TryHackMe rooms**

- [SSRF](https://tryhackme.com/room/ssrfhr)

**PortSwigger labs**

| # | Lab | Level | Status |
|---|---|---|---|
| 1 | Basic SSRF against the local server | Not specified | Not Solved |
| 2 | Basic SSRF against another back-end system | Apprentice | Not Solved |
| 3 | Blind SSRF with out-of-band detection | Practitioner | Not Solved |
| 4 | SSRF with blacklist-based input filter | Practitioner | Not Solved |

### Month 4: Common Web Vulnerabilities and Reporting

#### Week 1: SQL Injection

**Resources**

1. [Video 1](https://www.youtube.com/watch?v=jYuAP-veF4Y&list=PLsB1gqjeUAh_99a9LbVbxg-nBV79o0kW3&index=7)
2. [Video 2](https://www.youtube.com/watch?v=67OhK-ByVLI&list=PLsB1gqjeUAh_99a9LbVbxg-nBV79o0kW3&index=8)
3. [SQL Injection Playlist](https://www.youtube.com/playlist?list=PLuyTk2_mYISLaZC4fVqDuW_hOk0dd5rlf)

**TryHackMe rooms**

- [SQL Injection](https://tryhackme.com/room/sqlinjectionlm)

#### Week 2: Cross-Site Scripting (XSS)

**Resources**

1. [Video 1](https://youtu.be/xiw_O5shcK4?si=ZeOE0fHrzm-9HlRy)
2. [Video 2](https://www.youtube.com/watch?v=Qd7UuQyTLYw&list=PLsB1gqjeUAh_99a9LbVbxg-nBV79o0kW3&index=9)
3. [Video 3](https://www.youtube.com/watch?v=3G08COkUuYw&list=PLsB1gqjeUAh_99a9LbVbxg-nBV79o0kW3&index=10)

**TryHackMe rooms**

- [TryHackMe (task resource)](https://tryhackme.com/room/sqlinjectionlm)

**PortSwigger labs**

| # | Lab | Level |
|---|---|---|
| 1 | Reflected XSS into HTML context with nothing encoded | Apprentice |
| 2 | Stored XSS into HTML context with nothing encoded | Apprentice |
| 3 | DOM XSS in document.write sink using source location.search | Apprentice |
| 4 | DOM XSS in innerHTML sink using source location.search | Apprentice |
| 5 | DOM XSS in jQuery anchor href attribute sink using location.search source | Apprentice |
| 6 | DOM XSS in jQuery selector sink using a hashchange event | Apprentice |
| 7 | Reflected XSS into attribute with angle brackets HTML-encoded | Apprentice |
| 8 | Stored XSS into anchor href attribute with double quotes HTML-encoded | Apprentice |
| 9 | Reflected XSS into a JavaScript string with angle brackets HTML encoded | Apprentice |
| 10 | DOM XSS in document.write sink using source location.search inside a select element | Practitioner |
| 11 | DOM XSS in AngularJS expression with angle brackets and double quotes HTML-encoded | Practitioner |
| 12 | Reflected DOM XSS | Practitioner |
| 13 | Stored DOM XSS | Practitioner |
| 14 | Reflected XSS into HTML context with most tags and attributes blocked | Practitioner |
| 15 | Reflected XSS into HTML context with all tags blocked except custom ones | Practitioner |
| 16 | Reflected XSS with some SVG markup allowed | Practitioner |
| 17 | Reflected XSS in canonical link tag | Practitioner |

#### Week 3: XXE and SSTI

##### XML External Entity (XXE)

**Resources**

1. [XXE video](https://www.youtube.com/watch?v=vHJvKoBOEJo&list=PLsB1gqjeUAh_99a9LbVbxg-nBV79o0kW3&index=14)

**PortSwigger labs**

| # | Lab | Level |
|---|---|---|
| 1 | Exploiting XXE using external entities to retrieve files | Apprentice |
| 2 | Exploiting XXE to perform SSRF attacks | Apprentice |
| 3 | Blind XXE with out-of-band interaction | Practitioner |
| 4 | Blind XXE with out-of-band interaction via XML parameter entities | Practitioner |
| 5 | Exploiting blind XXE to exfiltrate data using a malicious external DTD | Practitioner |

##### Server-Side Template Injection (SSTI)

**Resources**

1. [SSTI video](https://www.youtube.com/watch?v=Th0QlXoDPhw&list=PLsB1gqjeUAh_99a9LbVbxg-nBV79o0kW3&index=11)

**TryHackMe rooms**

- [Learn SSTI](https://tryhackme.com/room/learnssti)

**PortSwigger labs**

| # | Lab | Level |
|---|---|---|
| 1 | Basic server-side template injection | Practitioner |
| 2 | Basic server-side template injection (code context) | Practitioner |
| 3 | Server-side template injection using documentation | Practitioner |
| 4 | Server-side template injection in an unknown language with a documented exploit | Practitioner |
| 5 | Additional LAB (name not provided in the original list) | Practitioner |

#### Week 4: OS Command Injection, Host Header Injection, and Reporting

##### OS Command Injection

**Resources**

1. [Video 1](https://youtu.be/Rq4LXdH8NK4?si=sxtcqPGUG4aSKsUa)
2. [Video 2](https://youtu.be/d3W2i52Bk9o?si=UXUuAClLgM--OVDA)

**PortSwigger labs**

| # | Lab | Level |
|---|---|---|
| 1 | OS command injection, simple case | Apprentice |
| 2 | Blind OS command injection with time delays | Practitioner |
| 3 | Blind OS command injection with output redirection | Practitioner |
| 4 | Blind OS command injection with out-of-band interaction | Practitioner |

##### Host Header Injection

**Resources**

1. [Host Header Injection video](https://youtu.be/klBJDJ5s3XM?si=f0W6cL6s5bVFjxjI)

**PortSwigger labs**

| # | Lab | Level |
|---|---|---|
| 1 | Basic password reset poisoning | Apprentice |
| 2 | Host header authentication bypass | Apprentice |

##### Penetration Testing Reports

**Resources**

1. [Penetration Testing Reports video](https://www.youtube.com/watch?v=N6dEXqHPzlI&list=PLsB1gqjeUAh_99a9LbVbxg-nBV79o0kW3&index=36)

**TryHackMe rooms**

- [Writing Pentest Reports](https://tryhackme.com/room/writingpentestreports)

## Weekly Tasks and Deliverables

### Month 1 Tasks

**Week 1 – HTML**

- [ ] Practice the HTML concepts covered in the course.

**Week 2 – JavaScript**

- [ ] Build a To-Do List project.

**Week 3 – SQL**

- [ ] Practice the SQL concepts covered in the course.

**Week 4 – PHP**

- [ ] Build the project demonstrated in the following playlist: [Project playlist](https://www.youtube.com/playlist?list=PL2fx_4nk5rCnxcBKIggrYEsG_7S5mdbdC)

### Month 2 Tasks

**Week 1 – Security Tools and Web Technologies**

- [ ] Download and set up Burp Suite.
- [ ] Take notes on the tools and their usage.
- [ ] Complete the assigned TryHackMe rooms.

**Week 2 – Reconnaissance**

- [ ] Document all commands demonstrated in the videos in a Google Doc.

**Week 3 – Broken Access Control and IDOR**

- [ ] Complete the assigned PortSwigger labs and TryHackMe room.
- [ ] Take screenshots of completed labs.
- [ ] Document important notes and payloads used.

**Week 4 – Information Disclosure and CORS**

- [ ] Complete all assigned PortSwigger labs.
- [ ] Take screenshots of completed labs.
- [ ] Document important notes and payloads used.

### Month 3 Tasks

**Week 1 – Path Traversal and File Upload**

- [ ] Complete all assigned PortSwigger labs.
- [ ] Take screenshots of completed labs.
- [ ] Document important notes and payloads used.

**Week 2 – Authentication and JWT**

- [ ] Complete all assigned PortSwigger labs.
- [ ] Take screenshots of completed labs.
- [ ] Document important notes and payloads used.

**Week 3 – OAuth and Business Logic Vulnerabilities**

- [ ] Complete all assigned PortSwigger labs.
- [ ] Take screenshots of completed labs.
- [ ] Document important notes and payloads used.

**Week 4 – CSRF and SSRF**

- [ ] Complete all assigned PortSwigger labs and TryHackMe rooms.
- [ ] Take screenshots of completed labs.
- [ ] Document important notes and payloads used.

### Month 4 Tasks

**Week 1 – SQL Injection**

- [ ] Solve all labs in the final playlist.
- [ ] Complete the assigned TryHackMe room.

**Week 2 – Cross-Site Scripting (XSS)**

- [ ] Complete all assigned PortSwigger labs.
- [ ] Take screenshots of completed labs.
- [ ] Document important notes and payloads used.

**Week 3 – XXE and SSTI**

- [ ] Complete all assigned PortSwigger labs and the TryHackMe room.
- [ ] Take screenshots of completed labs.
- [ ] Document important notes and payloads used.

**Week 4 – OS Command Injection, Host Header Injection, and Reporting**

- [ ] Complete the assigned labs and TryHackMe room.
- [ ] Take screenshots of completed labs.
- [ ] Document important notes and payloads used.

## Final Learning Outcomes

### Skills and knowledge covered


- **Month 1 – Web Development Fundamentals:** HTML; JavaScript; SQL; PHP
- **Month 2 – Web Security Fundamentals:** Security Tools and Web Technologies; Reconnaissance; Broken Access Control and IDOR; Information Disclosure and CORS
- **Month 3 – Advanced Web Vulnerabilities:** Path Traversal and File Upload; Authentication and JWT; OAuth and Business Logic Vulnerabilities; CSRF and SSRF
- **Month 4 – Common Web Vulnerabilities and Reporting:** SQL Injection; Cross-Site Scripting (XSS); XXE and SSTI; OS Command Injection, Host Header Injection, and Reporting

### Final practical outcomes


- A To-Do List project (JavaScript) and the PHP project built from the referenced playlist.
- Practice of the HTML and SQL concepts covered in the courses.
- Burp Suite downloaded and set up, with notes on the tools and their usage.
- All reconnaissance commands from the videos documented in a Google Doc.
- The assigned PortSwigger labs completed, with screenshots of completed labs.
- The assigned TryHackMe rooms completed: Hydra, Further Nmap, IDOR, CSRF Introduction, SSRF, SQL Injection, Learn SSTI and Writing Pentest Reports.
- Important notes and payloads documented for the labs.
