# eyeStudy Labs

eyeStudy Labs is a cybersecurity study workspace designed to help explore the concepts behind **asset visibility, device exposure, and security architecture across enterprise environments.**

The project focuses on understanding how organizations identify, monitor, and manage devices across modern infrastructure including corporate endpoints, IoT devices, operational technology, and unmanaged assets.

The goal is to better understand how **device visibility and exposure management platforms help security teams reduce risk across complex environments.**

---

# Purpose

Modern organizations struggle with knowing **what devices exist on their network and whether those devices are secure**.

Unknown, unmanaged, or poorly classified assets create significant security risk because they may:

- operate without security controls
- run outdated software
- bypass traditional endpoint protections
- introduce shadow IT into the environment

eyeStudy Labs explores how security platforms address these challenges by providing:

- asset discovery
- device classification
- risk context
- exposure visibility
- enforcement capabilities

---

# What This Project Explores

The study environment focuses on how organizations gain visibility into devices across their infrastructure.

Key areas include:

### Device Discovery

How security platforms identify assets across environments such as:

- corporate networks
- remote endpoints
- cloud environments
- operational technology networks
- IoT infrastructure

Discovery often relies on sources such as:

- DHCP logs
- network telemetry
- switch and router data
- endpoint agents
- API integrations

---

### Device Classification

Once devices are discovered, platforms attempt to classify them based on characteristics such as:

- operating system
- device type
- manufacturer
- network behavior
- security posture

This classification allows organizations to distinguish between:

- managed corporate devices
- unmanaged personal devices
- IoT and embedded devices
- servers and infrastructure
- operational technology assets

---

### Exposure Visibility

Understanding devices is only part of the challenge.

Security teams also need to evaluate **how exposed those devices are**.

Exposure can include factors such as:

- missing security agents
- outdated operating systems
- unpatched vulnerabilities
- risky network placement
- unknown device ownership

Platforms help security teams identify **which devices introduce the highest risk into the environment.**

---

### Vulnerability Context

Device visibility platforms often enrich asset data with vulnerability information such as:

- known CVEs
- outdated software versions
- missing patches
- insecure configurations

Combining asset visibility with vulnerability data allows teams to prioritize remediation efforts.

---

# Architecture Thinking

A key goal of this project is to understand how asset visibility fits within the broader security architecture.

In many environments, device exposure insights are enriched through integrations with other systems.

Examples include:

### Endpoint Security Platforms

Provide telemetry such as:

- endpoint alerts
- process activity
- malware detections
- device health status

---

### Identity Providers

Add user context including:

- authentication activity
- user identity
- access patterns
- privilege levels

---

### Network Infrastructure

Network devices provide critical telemetry such as:

- MAC address visibility
- VLAN assignments
- switch port mappings
- network segmentation context

---

### Vulnerability Management Platforms

These systems contribute information such as:

- vulnerability scans
- CVE scoring
- patch status
- exposure prioritization

---

# Example Security Workflow

A simplified exposure investigation may follow this flow:
## Example Security Workflow

1. **Device appears on network**

2. **Network telemetry identifies a previously unknown device**

3. **Device is classified based on behavior and attributes**

4. **Security platform evaluates posture and vulnerability data**

5. **Exposure risk is calculated**

6. **Security teams investigate or apply enforcement controls**

---

## Why This Matters

Organizations cannot secure what they cannot see.

Incomplete asset visibility leads to:

- unmanaged devices  
- shadow IT  
- unpatched systems  
- hidden attack surfaces  

By improving device visibility and exposure awareness, security teams can better understand the **true risk posture of their environment**.

---

## Technology Used

This study workspace was built using:

- Python  
- Gradio  
- structured security concept mapping  

---

## Intended Audience

This project is useful for:

- cybersecurity learners  
- technical account managers  
- security architects  
- customer success engineers  
- professionals preparing for roles in asset visibility or exposure management platforms  

---

## Focus Areas

The project centers around understanding concepts such as:

- asset visibility  
- device discovery  
- exposure management  
- vulnerability context  
- security architecture integrations  
