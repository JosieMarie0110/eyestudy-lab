### Project Status
Actively under development
# eyeStudy Labs

eyeStudy Labs is a cybersecurity study workspace built to help explore **asset visibility, integration context, exposure analysis, and security architecture mapping** across different environments.

Its designed for **scenario-based learning**, allowing users to study how different security integrations contribute context in environments such as healthcare, OT/IoT, education, and corporate office networks.

---

## Overview

Modern security teams rely on multiple tools working together to understand:

- what devices exist in the environment
- which assets are unmanaged or risky
- what context different integrations provide
- how that context supports investigation, triage, and response
- how technical findings map to operational and business outcomes

eyeStudy Labs helps break those relationships down into a more structured study experience.

---

## What the App Does

The app allows users to select:

- **Scenario**
- **Integration Type**
- **Integration Vendor**

Based on those selections, the app generates structured output showing:

- scenario summary
- key risks in that environment
- why visibility matters
- example findings
- recommended actions
- integration overview
- vendor-specific context
- example telemetry / sample data
- security architecture mapping
- example workflow
- business outcome mapping

---

## Example Scenarios

The app currently includes environments such as:

- **Medical / Healthcare**
- **Operational Technology / IoT**
- **School / Education**
- **Corporate Office**

These scenarios help show how the same integration type may matter differently depending on the environment.

---

## Integration Types Included

eyeStudy Labs currently includes examples for:

- **EDR**
- **SIEM**
- **Firewall**
- **NAC**
- **Identity / IAM**
- **Vulnerability Management**
- **Threat Intelligence**

Each integration type includes vendor-specific examples and sample context.

---

## Example Vendors

Some of the vendors represented in the app include:

- CrowdStrike
- Microsoft Defender
- SentinelOne
- Splunk
- Microsoft Sentinel
- QRadar
- Palo Alto
- Check Point
- Cisco ISE
- Aruba ClearPass
- Active Directory
- Microsoft Entra ID
- Okta
- Tenable
- Qualys
- Rapid7
- Anomali
- Recorded Future
- VirusTotal

---

## Business Value Focus

In addition to technical context, eyeStudy Labs also maps findings to broader outcomes such as:

- improved asset visibility
- faster investigations
- better remediation prioritization
- stronger segmentation decisions
- improved governance and ownership workflows
- reduced operational risk in sensitive environments

---

## Tech Stack

- Python
- Gradio
-Markdown-driven analysis output
- Custom CSS styling

---

## Run Locally

Clone the repository and start the application.

```bash
git clone <your-repo-url>
cd eyestudylab

If you are using a virtual environment:

python -m venv venv
source venv/bin/activate

If you are using a virtual environment:

python -m venv venv
source venv/bin/activate

## Project Goals

This project was built to support learning and interview preparation around topics such as:

- asset visibility  
- unmanaged device detection  
- integration ecosystem mapping  
- exposure analysis  
- vulnerability context  
- network access control  
- identity correlation  
- security operations workflows  
- architecture thinking  

The goal is to better understand how different security tools contribute context that helps teams investigate and prioritize risk.

---

## Future Improvements

Planned enhancements for the project include:

- side-by-side analysis panels  
- expanded integration types  
- deeper vendor comparisons  
- architecture diagrams for investigation workflows  
- interactive investigation scenarios  
- scoring or quiz modes for learning  
- improved visual layouts for security architecture mapping  

---

## Ideal Use Cases

eyeStudy Labs is designed to help with:

- cybersecurity interview preparation  
- studying integration ecosystems  
- understanding asset visibility platforms  
- learning exposure management concepts  
- exploring how different security tools enrich context  

It can also be used as a lightweight framework for exploring how different technologies interact within a security architecture.
