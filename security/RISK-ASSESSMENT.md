# RISK ASSESSMENT REPORT
## EEZ Bench Box 3 (BB3) Modular Test & Measurement Chassis

**Document Version**: 1.0  
**Date**: October 11, 2026  
**Prepared by**: Envox Security Team  
**Classification**: Internal - EU Cyber Resilience Act Compliance  
**Validity Period**: October 2026 – October 2027

---

## Executive Summary

**EEZ BB3** is an open-source modular Test & Measurement (T&M) device that combines hardware and firmware components for precision power supply, measurement, and automation capabilities. This risk assessment evaluates cybersecurity threats and vulnerabilities to ensure compliance with the **EU Cyber Resilience Act (CRA)** and establish a baseline for secure development practices.

### Key Findings

| Finding | Risk Level | Status |
|---------|-----------|--------|
| **Network connectivity without authentication** | 🔴 HIGH | Requires immediate mitigation |
| **Open-source software supply chain dependencies** | 🟠 MEDIUM-HIGH | Ongoing monitoring required |
| **Firmware update mechanism security** | 🟠 MEDIUM | Requires signature verification |
| **Hardcoded credentials (historical)** | 🔴 HIGH | Fixed in recent versions |
| **Web interface CSRF/XSS protection** | 🟡 MEDIUM | Partially addressed |
| **Local physical attack surface** | 🟡 MEDIUM | Inherent to device type |
| **MQTT integration without TLS enforcement** | 🟠 MEDIUM-HIGH | Configuration dependent |
| **Third-party module firmware security** | 🟡 MEDIUM | Modular design concern |

**Overall Risk Rating**: 🟠 **MEDIUM** (with controls in place)

**CRA Compliance Posture**: Product requires **Module A (Self-Assessment)** conformity assessment before December 11, 2027.

---

## 1. Product Overview & Scope

### 1.1 Product Description

**EEZ BB3** is a **modular Test & Measurement chassis** designed for:
- Precision power supply generation and measurement
- Automated testing and calibration
- Remote laboratory control and data acquisition
- DIY and professional benchtop applications

### 1.2 Hardware Architecture

| Component | Specifications | Security Relevance |
|-----------|-----------------|-------------------|
| **MCU** | STM32F769IIT6 (ARM Cortex-M7, 216 MHz) | 8 MB Flash, ARM TrustZone capable but not utilized |
| **Memory** | 2 MB SRAM, 8 GiB micro SD (user data) | Firmware & user configuration storage |
| **Display** | 4.3" TFT LCD (480 x 272 pixels) | Local UI for management & status |
| **Connectivity** | Ethernet PHY, USB, UART (serial) | Remote access attack surface |
| **Power Supply** | AC input via AUX board; output 0-40V/5A (DCP405) | Safety-critical power output |
| **Expansion** | DIB slot (up to 3 modules) | Modular firmware updates required |

### 1.3 Firmware Architecture

| Component | Technology | Open Source | Risk |
|-----------|----------|------------|------|
| **Base OS** | FreeRTOS v10.0.1+ | ✅ Yes (MIT License) | ⚠️ Dependency tracking |
| **Scripting** | MicroPython v1.12+ | ✅ Yes (MIT License) | ⚠️ Interpreter vulnerabilities |
| **Network Stack** | FreeRTOS+TCP | ✅ Yes (MIT License) | 🔴 Legacy TCP/IP implementation |
| **Web Server** | Custom C++ (embedded) | ✅ Yes (GPL-3.0) | 🟠 Input validation concerns |
| **MQTT Client** | Paho MQTT (embedded) | ✅ Yes (EPL/EDL) | 🟠 TLS configuration optional |
| **SCPI Parser** | Custom C implementation | ✅ Yes (GPL-3.0) | 🟡 Command injection potential |
| **Node-RED** | JavaScript runtime (external) | ✅ Yes (Apache 2.0) | 🟡 Depends on network isolation |

### 1.4 Supported Communication Protocols

- **SCPI** (Standard Commands for Programmable Instruments) – unencrypted over TCP/Ethernet
- **MQTT** – optional TLS/SSL support
- **USB Serial** – physical access required
- **Telnet** – unencrypted command interface
- **HTTP/REST** – web-based remote control
- **Node-RED** – JavaScript-based automation (external runtime)
- **EEZ Flow** – visual programming language (custom protocol)

---

## 2. Threat Analysis

### 2.1 Threat Categories

#### 2.1.1 **Network-Based Threats** (Severity: HIGH)

**Threat T1: Unauthenticated Remote Access**

- **Description**: SCPI and Telnet protocols accept commands without authentication
- **Attack Vector**: Network-based (Ethernet)
- **Impact**: 
  - Unauthorized power supply control
  - Measurement tampering
  - Device shutdown or damage
  - Measurement data exfiltration
- **Likelihood**: MEDIUM (requires network access, but no credentials checked)
- **CVSS Score**: 8.1 (HIGH)
- **CWE References**: CWE-306 (Missing Authentication), CWE-862 (Missing Authorization)

**Mitigation Status**:
- ⚠️ **Partial**: Basic network firewall can isolate device
- ⚠️ **Partial**: SSH option available (if enabled and credentials changed)
- ❌ **Not mitigated**: Default SCPI/HTTP access lacks authentication

**Recommended Controls**:
- Implement token-based authentication (OAuth2 or JWT) for HTTP/REST API
- Require password authentication for SCPI/Telnet connections
- Enforce TLS 1.2+ for all network communications
- Implement rate limiting on authentication failures

---

**Threat T2: Man-in-the-Middle (MitM) Attacks**

- **Description**: Network protocols transmit data without encryption (HTTP, SCPI plaintext)
- **Attack Vector**: Network-based (ARP spoofing, DNS hijacking, network sniffing)
- **Impact**:
  - Eavesdropping on measurement data
  - Command injection and device control manipulation
  - Firmware update interception
  - Credential capture
- **Likelihood**: MEDIUM-HIGH (depends on network environment)
- **CVSS Score**: 7.5 (HIGH)
- **CWE References**: CWE-295 (Improper Certificate Validation), CWE-327 (Inadequate Encryption)

**Mitigation Status**:
- ⚠️ **Partial**: HTTPS/TLS available for web interface
- ❌ **Not mitigated**: SCPI and Telnet transmit in plaintext
- ❌ **Not mitigated**: Firmware updates lack signature verification

**Recommended Controls**:
- Enforce HTTPS with TLS 1.2+ for all HTTP communication
- Implement SCPI over TLS (custom protocol wrapper)
- Sign firmware updates with cryptographic keys
- Validate firmware signatures before installation

---

**Threat T3: MQTT Injection & Data Breach**

- **Description**: MQTT broker connection may be configured without TLS; MQTT supports plaintext passwords
- **Attack Vector**: Network-based (MQTT broker compromise, network sniffing)
- **Impact**:
  - Measurement data exposure
  - Unauthorized device control via MQTT
  - Broker connection hijacking
- **Likelihood**: MEDIUM (configuration-dependent)
- **CVSS Score**: 7.2 (HIGH)
- **CWE References**: CWE-326 (Inadequate Encryption Strength), CWE-863 (Incorrect Authorization)

**Mitigation Status**:
- ⚠️ **Partial**: TLS support exists in Paho MQTT library
- ❌ **Not enforced**: TLS is optional; plaintext MQTT allowed
- ❌ **No validation**: MQTT broker certificate validation missing

**Recommended Controls**:
- Enforce TLS 1.2+ for all MQTT connections
- Require client certificate validation at broker
- Implement MQTT username/password authentication with strong credentials
- Document secure MQTT configuration in user manual

---

#### 2.1.2 **Firmware & Software Threats** (Severity: MEDIUM-HIGH)

**Threat T4: Vulnerable Third-Party Dependencies**

- **Description**: Firmware relies on open-source components with potential unpatched CVEs
- **Attack Vector**: Firmware compilation and runtime
- **Affected Components**:
  - FreeRTOS v10.0.1 (multiple known CVEs)
  - MicroPython v1.12 (interpreter vulnerabilities)
  - Paho MQTT (legacy versions with issues)
  - FreeRTOS+TCP (discontinued, limited support)
  - Custom SCPI parser (potential buffer overflows)

| Dependency | Current Version | Known Issues | Action Required |
|------------|-----------------|--------------|-----------------|
| FreeRTOS | v10.0.1+ | CVE-2022-24999 (memory leak), CVE-2019-12380 | ⚠️ Patch or upgrade |
| MicroPython | v1.12+ | Multiple memory safety issues | 🔴 Upgrade to v1.20+ |
| Paho MQTT | Embedded version | MQTT v5.0 compliance incomplete | 🟠 Test & validate |
| FreeRTOS+TCP | Latest | Long-term maintenance uncertain | 🟠 Consider LwIP replacement |

- **Impact**: Remote code execution, denial of service, information disclosure
- **Likelihood**: MEDIUM (requires specific attack conditions)
- **CVSS Score**: 7.8 (HIGH)
- **CWE References**: CWE-1035 (Vulnerable Components), CWE-426 (Untrusted Search Path)

**Mitigation Status**:
- ❌ **Not mitigated**: Dependency versions not regularly updated
- ⚠️ **Partial**: GitHub dependency scanning disabled
- ⚠️ **Partial**: Community contributions flag outdated dependencies

**Recommended Controls**:
- Implement Software Bill of Materials (SBOM) tracking
- Enable GitHub Dependabot for vulnerability alerts
- Establish dependency update policy (quarterly minimum)
- Create security patch testing procedure
- Plan FreeRTOS upgrade to latest LTS version

---

**Threat T5: Firmware Buffer Overflow / Memory Safety**

- **Description**: Custom C code (SCPI parser, network handlers) may contain buffer overflows
- **Attack Vector**: Malformed network packets, SCPI commands
- **Potentially Vulnerable Modules**:
  - SCPI command parser (unbounded string parsing)
  - HTTP request handler (header processing)
  - SD card file operations (path traversal)
  - MicroPython interpreter (memory management)

- **Impact**: Remote code execution, crash/DoS, data corruption
- **Likelihood**: MEDIUM-HIGH (C code without memory safety)
- **CVSS Score**: 8.6 (CRITICAL if RCE confirmed)
- **CWE References**: CWE-120 (Buffer Copy Without Bounds Check), CWE-129 (Improper Validation of Array Index)

**Mitigation Status**:
- ⚠️ **Partial**: Code review by community contributors
- ❌ **Not mitigated**: No static analysis or fuzzing
- ❌ **Not mitigated**: No memory protection (ASLR, DEP, stack canaries)

**Recommended Controls**:
- Implement static code analysis (Clang-Analyzer, Coverity)
- Add fuzzing tests for network protocol parsing
- Use compiler hardening flags (stack canaries, RELRO, PIE)
- Perform security code review of critical functions
- Add bounds checking to string operations

---

**Threat T6: Insecure Firmware Update Mechanism**

- **Description**: Firmware updates may lack cryptographic verification; no rollback protection
- **Attack Vector**: Network-based firmware upgrade, MitM during update
- **Scenarios**:
  - Attacker intercepts firmware file during download
  - Malicious firmware served by compromised update server
  - No signature verification before flashing
  - No rollback protection for corrupted updates

- **Impact**: Complete device compromise, malicious firmware installation
- **Likelihood**: MEDIUM (requires MitM or server compromise)
- **CVSS Score**: 8.8 (CRITICAL)
- **CWE References**: CWE-347 (Improper Verification of Cryptographic Signature), CWE-295 (Improper Certificate Validation)

**Mitigation Status**:
- ⚠️ **Partial**: Firmware size check exists
- ❌ **Not mitigated**: No signature verification
- ❌ **Not mitigated**: No secure boot mechanism
- ❌ **Not mitigated**: No rollback protection

**Recommended Controls**:
- Implement RSA-2048 or ECDSA firmware signature verification
- Store public keys in bootloader (secure firmware)
- Validate signatures before firmware flash
- Implement rollback protection with version checking
- Use HTTPS with certificate pinning for firmware downloads
- Sign all firmware releases in GitHub Actions

---

#### 2.1.3 **Supply Chain Threats** (Severity: MEDIUM)

**Threat T7: Modular Hardware Security**

- **Description**: Third-party DIB modules (DCP405, DCM224, MIO168, etc.) may have undocumented firmware or security issues
- **Attack Vector**: Malicious module firmware, hardware implants
- **Risk Areas**:
  - DCP405 (power module) – undocumented STM32 MCU firmware
  - DCM224 (dual buck converter) – bootloader security unknown
  - MIO168 (mixed I/O) – firmware update mechanism unvalidated
  - PREL6 (relay module) – command injection in firmware
  - SMX46 (switch matrix) – signal integrity vulnerabilities

- **Impact**: Unauthorized control of hardware, data exfiltration, physical safety risks
- **Likelihood**: MEDIUM (depends on module source)
- **CVSS Score**: 7.5 (HIGH)
- **CWE References**: CWE-1008 (Architectural Inconsistency), CWE-426 (Supply Chain)

**Mitigation Status**:
- ⚠️ **Partial**: Open-source hardware designs available for inspection
- ❌ **Not mitigated**: Module firmware sources not published (some modules)
- ❌ **Not mitigated**: No secure module authentication protocol

**Recommended Controls**:
- Publish firmware source code for all DIB modules
- Implement module authentication (e.g., EEPROM signature)
- Document bootloader security for each module type
- Establish module firmware update verification
- Require module CVE disclosure from third-party developers

---

**Threat T8: Dependency License & Malware Risk**

- **Description**: Open-source dependencies may introduce legal/malware risks
- **Attack Vector**: Software supply chain (compromised repository, typosquatting)
- **Affected Projects**:
  - FreeRTOS (Amazon-maintained, good security track record)
  - MicroPython (Community-maintained, security slower)
  - Node-RED (Node.js ecosystem – high-risk third-party packages)
  - EEZ Studio (custom IDE – integration risks)

- **Impact**: GPL license violations, malware infection, IP theft
- **Likelihood**: LOW (mature projects, but possible)
- **CVSS Score**: 5.3 (MEDIUM)
- **CWE References**: CWE-426 (Untrusted Search Path for Executable), CWE-1104 (Use of Unmaintained Third-Party Components)

**Mitigation Status**:
- ✅ **Mitigated**: GPL-3.0 license clearly stated
- ✅ **Mitigated**: Direct GitHub dependencies (not PyPI/NPM)
- ⚠️ **Partial**: No SBOM or dependency license audit

**Recommended Controls**:
- Create SBOM with license compliance documentation
- Implement automatic license scanning (FOSSA, Black Duck)
- Pin exact dependency versions in build system
- Scan binaries for malware signatures (VirusTotal)
- Audit third-party package integrity

---

#### 2.1.4 **Physical & Local Threats** (Severity: MEDIUM)

**Threat T9: Physical Access & SD Card Data**

- **Description**: Physical access to device allows SD card extraction and data access
- **Attack Vector**: Physical theft, rogue technician, lab assistant
- **Risks**:
  - SD card contains unencrypted measurement data
  - User configuration with potential secrets
  - Firmware reverse engineering possible
  - SD card replacement with malicious firmware

- **Impact**: Confidentiality breach (measurement data), firmware tampering
- **Likelihood**: MEDIUM (depends on lab security)
- **CVSS Score**: 6.2 (MEDIUM)
- **CWE References**: CWE-1220 (Insufficient Granularity of Access Control), CWE-306 (Missing Authentication)

**Mitigation Status**:
- ❌ **Not mitigated**: SD card unencrypted
- ❌ **Not mitigated**: No secure erase on data deletion
- ⚠️ **Partial**: Physical enclosure provides some protection

**Recommended Controls**:
- Implement SD card encryption (AES-256)
- Add secure erase mechanism for sensitive data
- Document secure disposal procedures
-
