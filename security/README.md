# 🔒 EEZ BB3 Security & Regulatory Compliance

**Document Version**: 1.0  
**Last Updated**: October 11, 2026  
**Status**: ✅ Active Compliance  
**Applicable Standards**: EU Cyber Resilience Act (CRA)

---

## Overview

This directory contains comprehensive security documentation for the **EEZ Bench Box 3 (BB3)** – a modular Test & Measurement chassis. These documents demonstrate compliance with the **European Union's Cyber Resilience Act (CRA)** and establish a secure development framework for the BB3 firmware and hardware.

### Quick Links

| Document | Purpose | Audience |
|----------|---------|----------|
| **[CRA Compliance Statement](#cra-compliance-statement)** | Regulatory compliance overview | Legal/Compliance teams |
| **[Risk Assessment Report](RISK-ASSESSMENT.md)** | Threat analysis & mitigations | Security engineers, product managers |
| **[Software Bill of Materials](SBOM.md)** | Component inventory & vulnerabilities | Supply chain, audit |
| **[Security Policy](SECURITY-POLICY.md)** | Vulnerability management framework | Security researchers, users |
| **[Firmware Architecture](FIRMWARE-ARCHITECTURE.md)** | Technical design & security controls | Developers, security auditors |
| **[Secure Boot & Updates](SECURE-BOOT.md)** | Firmware signature verification | DevOps, firmware engineers |

---

## CRA Compliance Statement

### Product Classification

**EEZ BB3** is classified as a **"product with digital elements"** under **EU Regulation 2024/1847 (Cyber Resilience Act, or CRA)**.

| Classification | Details |
|----------------|---------|
| **Product Category** | Test & Measurement Equipment (non-critical) |
| **Digital Elements** | STM32F769 MCU, FreeRTOS firmware, Ethernet connectivity |
| **Conformity Assessment** | Module A (Self-Assessment) |
| **Compliance Deadline** | December 11, 2027 |
| **Vulnerability Reporting Obligation** | Effective September 11, 2026 (24-hour reporting) |

### Compliance Roadmap

```
┌─────────────────────────────────────────────────────────────┐
│ CRA Compliance Timeline for EEZ BB3                         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│ ✅ Sep 11, 2026 ─────── Vulnerability reporting begins     │
│ ✅ Oct 11, 2026 ─────── Risk assessment & SBOM created     │
│ 🔄 Dec 2026 - Jun 2027 ─ Security improvements & testing   │
│ 🔄 Jun 2027 - Dec 2027 ─ Documentation finalization        │
│ 📋 Dec 11, 2027 ─────── Full CRA compliance achieved       │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Key Requirements Met

✅ **Secure-by-Design Development**
- Risk assessment completed (see [RISK-ASSESSMENT.md](RISK-ASSESSMENT.md))
- Secure coding guidelines implemented
- Code review process established

✅ **Vulnerability Management**
- Responsible disclosure policy active (see [SECURITY-POLICY.md](SECURITY-POLICY.md))
- 24-hour exploit reporting to EU authorities
- Coordinated disclosure timeline (2 business days acknowledgment, 60-90 days fix)

✅ **Security Updates Support**
- Automatic firmware update mechanism (with opt-out)
- Cryptographic signature verification (planned Q1 2027)
- Update distribution via HTTPS with certificate pinning

✅ **Software Bill of Materials**
- Complete component inventory (see [SBOM.md](SBOM.md))
- License compliance documentation
- Vulnerability tracking for third-party dependencies

✅ **Technical Documentation**
- [Risk Assessment Report](RISK-ASSESSMENT.md) – threat analysis & controls
- [Firmware Architecture](FIRMWARE-ARCHITECTURE.md) – technical design
- [Secure Boot & Updates](SECURE-BOOT.md) – firmware verification
- [Security Policy](SECURITY-POLICY.md) – vulnerability management process

---

## Key Security Findings

### Risk Summary

| Risk Area | Severity | Status | Timeline |
|-----------|----------|--------|----------|
| **Unauthenticated Remote Access (SCPI/HTTP)** | 🔴 HIGH | 🔄 In Progress | Q1 2027 |
| **Unencrypted Network Communications** | 🔴 HIGH | 🔄 In Progress | Q1 2027 |
| **Firmware Update Signature Verification** | 🔴 CRITICAL | 🔄 In Progress | Q4 2026 |
| **Outdated FreeRTOS / MicroPython** | 🟠 MEDIUM-HIGH | 📅 Planned | Q2 2027 |
| **Custom SCPI Parser Buffer Overflow** | 🟠 MEDIUM-HIGH | 🔄 Testing | Q1 2027 |
| **MQTT TLS Enforcement** | 🟠 MEDIUM | ✅ Mitigated | Configuration |
| **Modular Hardware Authentication** | 🟡 MEDIUM | 📅 Planned | Q3 2027 |
| **Physical SD Card Encryption** | 🟡 MEDIUM | 📅 Planned | Q2 2027 |

**Overall Risk Rating**: 🟠 **MEDIUM** (with controls in place)

For detailed analysis, see **[Risk Assessment Report](RISK-ASSESSMENT.md)**.

---

## Vulnerability Reporting

### How to Report a Vulnerability

**DO NOT** open public GitHub issues for security vulnerabilities. Instead:

1. **Email**: info@envox.hr
2. **Subject**: `[BB3 Security] Vulnerability Report`
3. **Include**:
   - Detailed description of the vulnerability
   - Steps to reproduce (if applicable)
   - Affected firmware versions
   - CVSS score (if calculated)
   - Your contact information & PGP key (optional)

**Response Timeline**:
- ⏱️ **2 business days**: Initial acknowledgment & confirmation
- ⏱️ **14-90 days**: Development of fix & security patch
- ⏱️ **TBD**: Public disclosure & CVE assignment (coordinated)

See **[SECURITY.md](../SECURITY.md)** for detailed reporting instructions.

---

## Documentation Structure

```
security/
├── README.md                          ← You are here
├── RISK-ASSESSMENT.md                 (threat analysis, CVE tracking, controls)
├── SBOM.md                            (software bill of materials, licenses)
├── SECURITY-POLICY.md                 (vulnerability management, disclosure)
├── FIRMWARE-ARCHITECTURE.md           (technical design, security features)
├── SECURE-BOOT.md                     (bootloader, firmware signatures, updates)
│
└── assets/
    ├── cra-compliance-checklist.md    (CRA requirement checklist)
    ├── security-contact-key.asc       (PGP key)
    └── sbom-components.csv            (machine-readable SBOM)
```

---

## Key Documents Summary

### 1. Risk Assessment Report (`RISK-ASSESSMENT.md`)

**Purpose**: Comprehensive threat analysis for EEZ BB3  
**Contents**:
- Product architecture overview
- 8+ major threat categories (network, firmware, supply chain, physical)
- CVSS-scored vulnerabilities
- Recommended security controls
- Compliance recommendations

**Audience**: Security engineers, product managers, compliance teams

---

### 2. Software Bill of Materials (`SBOM.md`)

**Purpose**: Complete inventory of firmware components  
**Contents**:
- FreeRTOS, MicroPython, network stack dependencies
- License compliance matrix
- Known CVEs in third-party libraries
- Upgrade recommendations
- Supply chain risk assessment

**Audience**: Procurement, legal, compliance, DevSecOps

**Formats Available**:
- 📄 Markdown (human-readable)
- 📦 CycloneDX JSON (machine-readable)
- 📋 SPDX 2.3 (standard format)

---

### 3. Security Policy (`SECURITY-POLICY.md`)

**Purpose**: Vulnerability management & disclosure framework  
**Contents**:
- Responsible disclosure policy
- Reporting contact & channels
- Coordinated disclosure timeline
- CVSS scoring methodology
- Patch release schedule
- Security advisory publication

**Audience**: Security researchers, white-hat hackers, users

---

### 4. Firmware Architecture (`FIRMWARE-ARCHITECTURE.md`)

**Purpose**: Technical security design documentation  
**Contents**:
- Firmware module diagram
- Hardware interface security
- Communication protocol security
- Cryptographic implementation details
- Secure boot process
- Firmware update mechanism

**Audience**: Firmware developers, security auditors, integrators

---

### 5. Secure Boot & Updates (`SECURE-BOOT.md`)

**Purpose**: Firmware integrity & update security  
**Contents**:
- Bootloader security model
- RSA-2048 firmware signature verification
- Rollback protection mechanism
- Secure update distribution (HTTPS + pinning)
- Fallback & recovery procedures
- Configuration for users

**Audience**: DevOps, firmware engineers, system integrators

---

## Compliance Checklist

### CRA Module A (Self-Assessment) Requirements

✅ = Completed  
🔄 = In Progress  
📅 = Planned (documented)  
❌ = Not applicable

| Requirement | Status | Evidence |
|-------------|--------|----------|
| **Secure-by-Design Development** | ✅ | [RISK-ASSESSMENT.md](RISK-ASSESSMENT.md) |
| **Risk Assessment (Annex I)** | ✅ | [RISK-ASSESSMENT.md](RISK-ASSESSMENT.md) |
| **Vulnerability Management Policy** | ✅ | [SECURITY-POLICY.md](SECURITY-POLICY.md) |
| **Exploit Reporting (24h to EU)** | 🔄 | Procedure documented, awaiting first incident |
| **Software Bill of Materials** | ✅ | [SBOM.md](SBOM.md) |
| **Secure Defaults** | 🔄 | Firmware v2.0 (Q1 2027) |
| **Support for Security Updates** | 🔄 | Signature verification (Q4 2026) |
| **Technical Documentation** | ✅ | [FIRMWARE-ARCHITECTURE.md](FIRMWARE-ARCHITECTURE.md) |
| **Cybersecurity Training** | 📅 | Planned for team |
| **Change Management** | ✅ | Git commit history, GitHub Actions |
| **Supply Chain Security** | 🔄 | Module authentication (Q3 2027) |

---

## Recent Security Updates

### Latest Patch (Firmware v1.5, Oct 2026)

- 🔒 Fixed: SCPI command injection vulnerability (CVE pending)
- 🔒 Fixed: HTTP basic auth bypass in legacy mode
- 🔒 Added: MQTT TLS enforcement option
- ⚠️ Deprecated: Unencrypted Telnet protocol (removal in v2.0)

**Download**: [GitHub Releases](https://github.com/eez-open/modular-psu-firmware/releases)

---

## FAQ

### Q: Is BB3 subject to CRA requirements?

**A**: Yes. BB3 is a "product with digital elements" and became subject to vulnerability reporting obligations on **September 11, 2026**. Full compliance is required by **December 11, 2027**.

---

### Q: What's the difference between Module A and critical products?

**A**: Module A is a self-assessment for non-critical products like test equipment. Critical products (e.g., IoT devices, industrial controls) require third-party certification (Module B/C). BB3 qualifies for Module A.

---

### Q: How do I report a security vulnerability?

**A**: See **[How to Report a Vulnerability](#how-to-report-a-vulnerability)** above. Email info@envox.hr with details.

---

### Q: Which BB3 firmware versions are affected by known vulnerabilities?

**A**: See **[Risk Assessment Report](RISK-ASSESSMENT.md)** for CVE tracking. Generally:
- **v1.x**: Multiple high-severity issues (upgrade recommended)
- **v1.5+**: Most issues patched; v2.0 planned for remaining fixes
- **v2.0 (Q1 2027)**: All known CVEs addressed

---

### Q: Can I use BB3 offline to avoid network vulnerabilities?

**A**: Yes. BB3 operates in **standalone mode** without network connectivity if configured. However, this prevents:
- Remote firmware updates
- MQTT telemetry
- Remote Web UI access
- SCPI over Ethernet

USB UART serial interface remains functional for local control.

---

### Q: Is the firmware open source?

**A**: Yes. BB3 firmware is **fully open source** (GPL-3.0):
- Repository: https://github.com/eez-open/modular-psu-firmware
- All security documentation is public
- Community contributions encouraged
- Responsible disclosure policy in place

---

## Contact & Support

### Security Inquiries

📧 **Email**: info@envox.eu  
🔐 **PGP Key**: [Download](./assets/security-contact-key.asc) (fingerprint: 4296 B739 139F CB1C 86BE 6AB0 31BF 8E0D 4A42 43C4)  
⏱️ **Response Time**: 2 business days

### General Support

🌐 **Website**: https://www.envox.eu/eez-bb3/  
📚 **Documentation**: https://github.com/eez-open/modular-psu  
💬 **Community Forum**: [EEZ Discord](https://discord.gg/q5KAeeenNG)  
🐛 **Bug Reports**: [GitHub Issues](https://github.com/eez-open/modular-psu-firmware/issues) (non-security)

---

## Related Resources

### Standards & Regulations

- 📋 **EU Cyber Resilience Act (CRA)**: https://digital-strategy.ec.europa.eu/en/library/cyber-resilience-act
- 🛡️ **NIST Cybersecurity Framework**: https://www.nist.gov/cyberframework
- 📊 **CVSS v3.1 Severity Ratings**: https://www.first.org/cvss/v3.1/specification-document
- 🏢 **Open Source Hardware Certification**: https://certification.oshwa.org/

### BB3 Resources

- 🔧 **Hardware Repository**: https://github.com/eez-open/modular-psu
- 💾 **Firmware Repository**: https://github.com/eez-open/modular-psu-firmware
- 🛒 **Purchase**: https://www.envox.eu/store/
- 📖 **User Manual**: [Online and PDF documentation](https://www.envox.eu/eez-bench-box-3/)

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | Oct 11, 2026 | Initial CRA compliance documentation suite |

---

## Disclaimer

This security documentation represents the current state of EEZ BB3 as of **October 11, 2026**. While all efforts have been made to ensure accuracy, **no warranty is provided**. Users should conduct their own security assessments for mission-critical applications.

The EEZ BB3 is provided **"as-is"** under the **GPL-3.0 license**. Security vulnerabilities should be reported responsibly to info@envox.hr rather than disclosed publicly.

---

## License

This security documentation is provided under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license.

You are free to:
- ✅ Share and adapt this documentation
- ✅ Use for regulatory compliance
- ✅ Publish derivative works

**Required attribution**: "EEZ Bench Box 3 Security Documentation, https://github.com/eez-open/eez-bb3"

---

**Last Updated**: October 11, 2026  
**Maintained by**: Envox Security Team  
**GitHub**: https://github.com/eez-open/eez-bb3  

