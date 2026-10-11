# Security Policy

## Reporting a Vulnerability

We take the security of EEZ BB3 seriously. If you discover a security vulnerability in our product, firmware, or documentation, please help us by responsibly disclosing it to our security team rather than publicly discussing the issue.

### How to Report

**Please do NOT create a public GitHub issue for security vulnerabilities.**

Instead, report security vulnerabilities by emailing:

**info@envox.hr**

Include the following information in your report:

- **Description**: A clear description of the vulnerability and its potential impact
- **Affected Component(s)**: Which part of EEZ BB3 is affected (firmware version, hardware revision, specific module, etc.)
- **Steps to Reproduce**: Detailed steps to reproduce the vulnerability, if applicable
- **Proof of Concept**: Example code, configuration, or screenshots demonstrating the vulnerability (if safe to share)
- **Potential Impact**: Assessment of severity and affected systems
- **Your Contact Information**: Your name, email, and PGP key (optional but recommended for sensitive reports)

### PGP Key

For highly sensitive security reports, you may encrypt your email using our PGP key: [Download](security/assets/security-contact-key.asc) (fingerprint: 4296 B739 139F CB1C 86BE 6AB0 31BF 8E0D 4A42 43C4)


## Vulnerability Handling Process

### Our Commitment

We are committed to addressing reported vulnerabilities promptly and transparently. Our security team will:

1. **Acknowledge receipt** of your report within **2 business days**
2. **Evaluate the vulnerability** and assess its severity within **7 calendar days**
3. **Develop and test a fix** for confirmed vulnerabilities
4. **Prepare a security update** and coordinate its release
5. **Credit the reporter** publicly (unless you request anonymity)

### Timeline for Coordinated Disclosure

| Phase | Timeline | Description |
|-------|----------|-------------|
| **Initial Response** | ≤ 2 business days | Acknowledge receipt and confirm we received your report |
| **Vulnerability Assessment** | ≤ 7 calendar days | Confirm whether the report describes a valid vulnerability |
| **Fix Development** | ≤ 60 calendar days | Develop, test, and validate a security patch |
| **Patch Release Preparation** | ≤ 90 calendar days | Prepare firmware update and supporting documentation |
| **Public Disclosure** | 90 calendar days | Publish advisory, security update, and acknowledge reporter |

**Note:** Timeline may be extended if complex development or cross-platform testing is required. We will communicate any delays to the reporter.

### Severity Classifications

We classify vulnerabilities according to the following severity levels:

#### Critical (CVSS 9.0–10.0)

- **Example**: Remote code execution, complete loss of confidentiality/integrity/availability
- **Action**: Fix within 60 days; emergency out-of-cycle release may be issued
- **Public Disclosure**: Advisory published immediately upon patch release

#### High (CVSS 7.0–8.9)

- **Example**: Privilege escalation, unauthorized access to sensitive data, complete bypass of security mechanism
- **Action**: Fix within 60 days; included in next scheduled release
- **Public Disclosure**: Advisory published upon patch release

#### Medium (CVSS 4.0–6.9)

- **Example**: Partial compromise of confidentiality/integrity, information disclosure, denial of service
- **Action**: Fix within 90 days; included in upcoming release or maintenance update
- **Public Disclosure**: Advisory published upon patch release

#### Low (CVSS 0.1–3.9)

- **Example**: Minor information disclosure, limited denial of service, requires user interaction
- **Action**: Fix in next available release; may be batched with other updates
- **Public Disclosure**: Advisory published upon patch release

---

## Coordinated Disclosure Agreement

By submitting a vulnerability report, you agree to:

1. **Not publicly disclose the vulnerability** until we have released a security update or 90 calendar days have passed since your initial report, whichever comes first
2. **Not exploit the vulnerability** beyond what is necessary to confirm its existence
3. **Limit knowledge** of the vulnerability to individuals who need to know to assist in the disclosure process
4. **Work cooperatively** with our security team to resolve the vulnerability
5. **Allow us to coordinate disclosure** with affected parties, including users and downstream projects

We agree to:

1. **Work diligently** to develop and release a fix within the timelines specified above
2. **Keep you informed** throughout the process with regular status updates
3. **Credit you publicly** in the security advisory (unless you request anonymity)
4. **Not pursue legal action** against researchers conducting good-faith security research within the scope of this policy

---

## Scope of This Policy

This policy applies to:

✅ **In Scope:**

- EEZ BB3 firmware (all versions available on GitHub)
- EEZ BB3 hardware design files and documentation
- Integrated modules and firmware components (DCP405, DCM224, etc.)
- Software libraries and tools distributed by Envox for use with EEZ BB3
- EEZ Web Store and official distribution channels

❌ **Out of Scope:**

- Third-party applications or firmware not maintained by Envox
- Vulnerabilities in upstream open-source projects (report directly to those projects)
- Social engineering, phishing, or attacks targeting Envox personnel
- Vulnerabilities in non-standard or heavily modified firmware
- Physical security issues or side-channel attacks (consult us first)

---

## Safe Harbor

We appreciate your responsible disclosure and will not take legal action against security researchers who:

1. Follow this vulnerability disclosure policy
2. Act in good faith to discover and report vulnerabilities
3. Do not exceed the scope of authorized security testing
4. Do not compromise privacy or data of other users
5. Avoid unnecessary disruption to our services or products

---

## Security Updates and Patches

### Firmware Updates

- **Availability**: Security patches are released via the official EEZ BB3 update mechanism
- **Announcement**: Security advisories are published on our GitHub repository and website
- **Installation**: Users are encouraged to update to the latest firmware version promptly

### End of Life & Long-Term Support

- **Hardware Revisions**: We commit to providing security updates for a minimum of **5 years** from the hardware revision release date
- **Firmware**: Critical security patches will be made available as long as the hardware is actively supported
- **Legacy Versions**: Older firmware versions may receive limited or no security updates; users are encouraged to upgrade

---

## Known Security Advisories

A comprehensive list of past security advisories is available at:

📋 **https://github.com/eez-open/modular-psu/security/advisories**

---

## Questions or Feedback?

If you have questions about this security policy or suggestions for improvements, please contact:

**info@envox.hr**

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-10-11 | Initial security policy release |

---

## References

- [OWASP Vulnerability Disclosure Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Vulnerability_Disclosure_Cheat_Sheet.html)
- [EU Cyber Resilience Act (CRA)](https://digital-strategy.ec.europa.eu/en/library/cyber-resilience-act)
- [CVSS v3.1 Specification](https://www.first.org/cvss/v3.1/specification-document)

---

*Last Updated: October 11, 2026*  
*Next Review: October 11, 2027*  

