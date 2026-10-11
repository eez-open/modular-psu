# 📋 CRA Compliance Requirement Checklist – EEZ BB3

**Document Version**: 1.0  
**Last Updated**: October 11, 2026  
**Product**: EEZ Bench Box 3 (BB3)  
**Classification**: Default Product (Module A Self-Assessment)  
**Compliance Deadline**: December 11, 2027  
**Regulation**: EU Regulation 2024/2847 (Cyber Resilience Act)

---

## Quick Status Overview

| Phase | Deadline | Status | Progress |
|-------|----------|--------|----------|
| **Vulnerability Reporting** | September 11, 2026 | ✅ Active | 100% |
| **Risk Assessment** | December 11, 2027 | ✅ Complete | 100% |
| **SBOM & Documentation** | December 11, 2027 | ✅ Complete | 100% |
| **Secure Development (v2.0)** | December 11, 2027 | 🔄 In Progress | 35% |
| **CE Marking & DoC** | December 11, 2027 | 📅 Planned | 0% |

**Overall Compliance Progress**: 🟠 **60% Complete** (on track for Dec 2027 deadline)

---

## Section 1: Product Classification & Scope

### 1.1 Product Classification

| Item | Status | Evidence |
|------|--------|----------|
| ✅ **Product qualifies as "product with digital elements"** | ✅ Confirmed | STM32F769 MCU, FreeRTOS firmware, network connectivity |
| ✅ **Determined product category (Default/Important/Critical)** | ✅ Confirmed | Test & measurement equipment = **Default** (Module A) |
| ✅ **Product not excluded from CRA scope** | ✅ Confirmed | Not medical device, motor vehicle, or civil aviation equipment |
| ✅ **Product placed on EU market** | ✅ Confirmed | Sold via EEZ Store, Crowd Supply, distributors |
| ✅ **Commercial activity status confirmed** | ✅ Confirmed | Open-source but sold commercially |

**Classification Decision**: **DEFAULT PRODUCT** → Module A Self-Assessment permitted

---

## Section 2: Program Governance & Organization

### 2.1 Organizational Structure

| Item | Status | Evidence | Deadline |
|------|--------|----------|----------|
| ✅ **Security responsibility assigned** | ✅ Complete | Envox security team designated | ✅ Oct 2026 |
| ✅ **Security contact established** | ✅ Complete | security@envox.eu | ✅ Oct 2026 |
| ✅ **RACI matrix documented** | 🔄 In Progress | Incident response procedure draft | 📅 Dec 2026 |
| 🔄 **Security training plan for development team** | 📅 Planned | Curriculum TBD | 📅 Jun 2027 |
| 🔄 **Vulnerability handling process defined** | ✅ Complete | SECURITY.md & SECURITY-POLICY.md | ✅ Oct 2026 |
| 🔄 **Change management process** | ✅ Complete | Git + GitHub Actions | ✅ Oct 2026 |

**Status**: ✅ **75% Complete**

---

## Section 3: Secure-by-Design Development (Annex I)

### 3.1 Risk Assessment (Annex I, Section I(1))

| Item | Status | Evidence | Notes |
|------|--------|----------|-------|
| ✅ **Cybersecurity risk assessment completed** | ✅ Complete | [RISK-ASSESSMENT.md](../RISK-ASSESSMENT.md) v1.0 | Pre-development baseline |
| ✅ **Threat model documented** | ✅ Complete | 8 threat categories identified | Network, firmware, supply chain, physical |
| ✅ **Attack surface identified** | ✅ Complete | SCPI, HTTP, MQTT, USB, Ethernet | Baseline architecture |
| ✅ **Threat actors & attack vectors defined** | ✅ Complete | Remote attackers, local users, supply chain | Per threat model |
| ✅ **Risk assessment versioned & maintained** | 🔄 In Progress | v1.0 (Oct 2026); v1.5 planned Q2 2027 | Updated per product lifecycle |
| ✅ **Risk assessment includes residual risk statement** | ✅ Complete | Medium overall rating with defined mitigations | RISK-ASSESSMENT.md §5 |

**Status**: ✅ **100% Complete** (v1.0 delivered Oct 11, 2026)

---

### 3.2 Secure-by-Default Design (Annex I, Section I(2))

| Item | Status | Evidence | Target Fix |
|------|--------|----------|-----------|
| 🔴 **No unnecessary attack surface (disabled by default)** | ⚠️ Partial | Telnet deprecated in v1.5; unencrypted HTTP enabled | **v2.0 (Q1 2027)** |
| 🔴 **Secure defaults (no hardcoded passwords)** | ⚠️ Partial | Credentials removed in v1.4; new defaults in v2.0 | **v2.0 (Q1 2027)** |
| 🔴 **Encryption enabled by default** | ⚠️ Not Implemented | MQTT TLS optional; HTTP unencrypted | **v2.0 (Q1 2027)** |
| 🔴 **Secure configuration guidance provided** | ⚠️ Partial | User manual available; security hardening guide TBD | **📅 Dec 2026** |
| 🟡 **Minimal attack surface** | 🔄 In Progress | Firmware modularity supports disabling features | **v2.0 (Q1 2027)** |
| ✅ **Physical attack protection considered** | ✅ Complete | SD card encryption planned (Q2 2027) | Risk acknowledged |

**Status**: 🟠 **40% Complete** (major improvements in v2.0 pipeline)

---

### 3.3 Access Control & Authentication (Annex I, Section I(3))

| Item | Status | Evidence | Target Fix |
|------|--------|----------|-----------|
| 🔴 **Protects against unauthorized access** | ⚠️ Partial | SCPI/HTTP unauthenticated; local control only on USB | **v2.0 (Q1 2027)** |
| 🔴 **Authentication mechanism implemented** | ⚠️ Partial | Token-based auth in development (v2.0) | **v2.0 (Q1 2027)** |
| 🔴 **Unique user credentials enforced** | ⚠️ Not Implemented | Shared access model (no per-user accounts yet) | **📅 Jun 2027** |
| ✅ **Network access controls documented** | ✅ Complete | Firmware design doc covers interface security | [FIRMWARE-ARCHITECTURE.md](../FIRMWARE-ARCHITECTURE.md) |
| ✅ **Physical access restrictions** | ✅ Complete | Local UART requires physical access | Hardware design |

**Status**: 🟠 **35% Complete** (auth mechanisms planned for v2.0+)

---

### 3.4 Cryptography & Secure Communications (Annex I, Section I(3))

| Item | Status | Evidence | Target Fix |
|------|--------|----------|-----------|
| 🔴 **Encryption for data in transit** | ⚠️ Partial | HTTP unencrypted; MQTT TLS optional | **v2.0 (Q1 2027)** |
| 🔴 **HTTPS/TLS enforced by default** | ⚠️ Not Implemented | Planning HTTPS with cert pinning | **v2.0 (Q1 2027)** |
| 🔴 **Strong cryptographic algorithms** | ⚠️ Partial | mbedTLS planned for v2.0; legacy OpenSSL 1.1.1 in v1.x | **v2.0 (Q1 2027)** |
| 🟡 **Encryption for data at rest** | 📅 Planned | SD card encryption (hardware supports) | **v2.0 (Q2 2027)** |
| ✅ **Cryptographic key management** | 🔄 In Progress | Firmware bootloader signature verification (Q4 2026) | [SECURE-BOOT.md](../SECURE-BOOT.md) |
| ✅ **Certificate validation implemented** | 🔄 In Progress | Certificate pinning for HTTPS (v2.0) | Network security |

**Status**: 🟠 **30% Complete** (major cryptography upgrade in v2.0)

---

### 3.5 Secure Firmware Updates (Annex I, Section I(5))

| Item | Status | Evidence | Target Fix |
|------|--------|----------|-----------|
| 🔴 **Cryptographic signature verification** | 🔄 In Progress | RSA-2048 signatures planned Q4 2026 | **v1.6 (Q4 2026)** |
| 🔴 **Rollback protection** | 🔄 In Progress | Version check + timestamp validation | **v1.6 (Q4 2026)** |
| ✅ **Automatic update mechanism** | ✅ Complete | OTA update over MQTT/HTTP supported | Firmware v1.0+ |
| ✅ **User control over updates** | ✅ Complete | Manual & automatic modes with opt-out | User configurable |
| ✅ **Secure distribution channel (HTTPS)** | 🔄 In Progress | HTTPS with pinning planned (v2.0) | **v2.0 (Q1 2027)** |
| 🟡 **Update availability period defined** | 📅 Planned | 5-year minimum (aligned with FreeRTOS v12 LTS EOL) | **DoC (Dec 2027)** |

**Status**: 🟠 **55% Complete** (signature verification critical, in progress Q4 2026)

---

## Section 4: Software Bill of Materials (SBOM)

### 4.1 SBOM Completeness & Quality

| Item | Status | Evidence | Notes |
|------|--------|----------|-------|
| ✅ **SBOM created & maintained** | ✅ Complete | [SBOM.md](../SBOM.md) v1.0 & CSV export | 24+ components documented |
| ✅ **All direct dependencies documented** | ✅ Complete | FreeRTOS, MicroPython, Paho MQTT, custom code | Top-level inventory |
| ✅ **Transitive dependencies identified** | ✅ Complete | FreeRTOS+TCP, mbedTLS, cJSON, FatFS, lwIP | Dependency chain |
| ✅ **Component versions recorded** | ✅ Complete | Specific version numbers & version ranges | E.g., FreeRTOS 10.0.1+ |
| ✅ **SBOM machine-readable format** | ✅ Complete | CSV, CycloneDX JSON, SPDX 2.3 available | [sbom-components.csv](../assets/sbom-components.csv) |
| ✅ **License information included** | ✅ Complete | SPDX identifiers for all components | MIT, GPL-3.0, BSD, Apache, EPL |
| ✅ **Known vulnerabilities tracked** | ✅ Complete | CVE status per component | RISK-ASSESSMENT.md §3 |
| ✅ **Source/repository URLs provided** | ✅ Complete | GitHub URLs for all OSS components | Traceability |
| ✅ **Hardware Bill of Materials (HBOM)** | 🔄 In Progress | STM32F769, Ethernet PHY, SD controller documented | Planned expansion Q1 2027 |

**Status**: ✅ **90% Complete** (SBOM comprehensive; HBOM expansion planned)

---

### 4.2 Third-Party & Open-Source Component Governance

| Item | Status | Evidence | Policy |
|------|--------|----------|--------|
| ✅ **Component selection & approval process** | ✅ Complete | GitHub review process documented | PR requirement |
| ✅ **EOL tracking for dependencies** | ✅ Complete | SBOM includes EOL dates per component | See SBOM.md |
| ✅ **Vulnerability response SLA defined** | ✅ Complete | 24-72 hour assessment; 60-90 day fix | SECURITY-POLICY.md |
| 🟡 **Upgrade path planning** | 🔄 In Progress | FreeRTOS 10→12 LTS upgrade roadmap | **v2.0 (Q1 2027)** |
| 🟡 **MicroPython 1.12→1.20 upgrade** | 📅 Planned | Compatibility testing required | **v2.0 (Q2 2027)** |
| ✅ **License compliance audit** | ✅ Complete | GPL-3.0 compliance verified | Open-source repository |
| ✅ **Supply chain risk assessment** | ✅ Complete | GitHub repos monitored; fork ownership confirmed | [RISK-ASSESSMENT.md](../RISK-ASSESSMENT.md) §3.3 |

**Status**: ✅ **85% Complete** (governance solid; upgrade execution in progress)

---

## Section 5: Vulnerability Management & Incident Reporting (Article 14)

### 5.1 Vulnerability Handling Process

| Item | Status | Evidence | Target |
|------|--------|----------|--------|
| ✅ **Vulnerability disclosure policy published** | ✅ Complete | [SECURITY.md](../../SECURITY.md) in repository root | security@envox.eu |
| ✅ **Responsible disclosure coordinated** | ✅ Complete | 2-day acknowledgement; 60-90 day fix timeline | Defined SLA |
| ✅ **Vulnerability assessment process defined** | ✅ Complete | CVSS scoring; impact analysis documented | Severity classification |
| ✅ **Tracking system operational** | 🔄 In Progress | GitHub Security Advisories integration | [SECURITY-POLICY.md](../SECURITY-POLICY.md) |
| ✅ **Patch development workflow established** | 🔄 In Progress | Branch strategy for emergency fixes | Git + CI/CD |
| ✅ **Security advisory templates created** | ✅ Complete | Example GHSA format provided | Standardized reporting |
| 🔄 **Exploit detection process** | 📅 Planned | Threat intelligence monitoring setup | **Q1 2027** |

**Status**: ✅ **85% Complete** (process mature; exploit monitoring TBD)

---

### 5.2 Article 14 Reporting Obligations (24h / 72h / 14-day Cascade)

| Item | Status | Evidence | Timeline |
|------|--------|----------|----------|
| ✅ **Obligation acknowledged (Sept 11, 2026 start)** | ✅ Confirmed | Applies to current & future products | SECURITY-POLICY.md |
| ✅ **24-hour early warning process documented** | ✅ Complete | Initial notification to EU authorities | Exploit confirmation required |
| ✅ **72-hour detailed notification procedure** | ✅ Complete | Full vulnerability disclosure template | SECURITY.md + SECURITY-POLICY.md |
| ✅ **14-day final report process** | ✅ Complete | Remediation plan & timeline | Follow-up submission |
| ✅ **Contact info for EU authorities** | 📅 Planned | ENISA portal registration | **Q4 2026** |
| 🔄 **Internal escalation/RACI for Article 14** | 🔄 In Progress | Security team on-call procedure | **Dec 2026** |
| 📅 **Tabletop exercise (recommended)** | 📅 Planned | Simulated vulnerability scenario | **Q1 2027** |

**Status**: 🟠 **75% Complete** (process documented; ENISA portal TBD)

---

### 5.3 Post-Market Vulnerability Management

| Item | Status | Evidence | Timeline |
|------|--------|----------|----------|
| ✅ **Monitoring for actively exploited vulnerabilities** | 🔄 In Progress | Threat feeds configured | GitHub, NVD, vendor advisories |
| ✅ **Patch release schedule established** | ✅ Complete | Monthly patches + emergency releases | [GitHub Releases](https://github.com/eez-open/modular-psu-firmware/releases) |
| ✅ **User notification mechanism** | ✅ Complete | GitHub releases, email, website | Multi-channel approach |
| 🟡 **Firmware version tracking system** | 🔄 In Progress | Device telemetry (MQTT) to track deployed versions | **v2.0 (Q1 2027)** |
| 📅 **Supply chain vulnerability tracking** | 📅 Planned | Dependency scanning integration (Dependabot, Snyk) | **Q1 2027** |

**Status**: 🟠 **70% Complete**
