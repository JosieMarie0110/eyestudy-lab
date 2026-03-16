import gradio as gr

APP_TITLE = "eyeStudy Labs"
APP_SUBTITLE = (
    "Cybersecurity study workspace for scenario-based integration mapping, vendor context, "
    "architecture flow, and example telemetry used in security investigations."
)

# =========================================================
# SCENARIOS
# =========================================================

SCENARIOS = {
    "Medical / Healthcare": {
        "summary": (
            "Healthcare environments combine traditional IT, clinical workstations, medical IoT, "
            "shared infrastructure, and operationally sensitive systems."
        ),
        "risks": [
            "Unmanaged clinical and biomedical devices",
            "Legacy operating systems",
            "Patient safety and operational disruption risk",
            "Shared network paths between IT and medical assets",
        ],
        "value": (
            "Visibility matters because unknown or weakly classified devices in clinical environments "
            "can increase operational risk, slow investigations, and complicate segmentation decisions."
        ),
        "findings": [
            "Unknown infusion-support device observed in a clinical subnet",
            "Unsupported workstation communicating with sensitive systems",
            "Smart camera with incomplete ownership data",
        ],
        "actions": [
            "Validate ownership and business criticality of unmanaged assets",
            "Review segmentation around clinical systems",
            "Correlate findings with NAC, firewall, SIEM, and ITSM workflows",
            "Prioritize unsupported systems for remediation or containment",
        ],
    },
    "Operational Technology / IoT": {
        "summary": (
            "OT and IoT environments often include controllers, sensors, badge systems, cameras, "
            "industrial assets, and devices that rely heavily on passive discovery."
        ),
        "risks": [
            "Devices that cannot run security agents",
            "Weak ownership or maintenance visibility",
            "Shared IT/OT paths that increase blast radius",
            "Operational disruption from unmanaged or misclassified assets",
        ],
        "value": (
            "Visibility matters because many OT and IoT assets cannot support agents, so teams rely on "
            "network context, integrations, and careful operational awareness to understand risk."
        ),
        "findings": [
            "Unknown industrial controller seen on a production segment",
            "Vendor maintenance laptop with incomplete posture data",
            "Shared infrastructure path between corporate IT and OT zones",
        ],
        "actions": [
            "Validate device role and maintenance ownership",
            "Review transient device exceptions and OT-safe controls",
            "Strengthen passive discovery and segmentation mapping",
            "Document operational dependencies before enforcement changes",
        ],
    },
    "School / Education": {
        "summary": (
            "Education environments are high-churn and often contain student devices, staff endpoints, "
            "labs, dorm equipment, printers, cameras, and unmanaged systems."
        ),
        "risks": [
            "Student-owned and BYOD devices",
            "Dorm and classroom shared infrastructure",
            "Frequent user and device turnover",
            "Visibility gaps across transient or unmanaged assets",
        ],
        "value": (
            "Visibility matters because ownership changes quickly in campus environments, and unmanaged "
            "or shared devices can create investigation and segmentation challenges."
        ),
        "findings": [
            "Unknown gaming console detected in dorm network",
            "Smart camera with incomplete classification confidence",
            "Dorm printer associated with multiple user patterns",
        ],
        "actions": [
            "Validate ownership of unknown and transient devices",
            "Use multiple telemetry sources to improve classification confidence",
            "Align findings with SIEM, firewall, NAC, and ITSM workflows",
            "Restrict unmanaged assets where appropriate",
        ],
    },
    "Corporate Office": {
        "summary": (
            "Corporate office environments include laptops, phones, printers, collaboration devices, "
            "servers, SaaS access, identity systems, and remote user workflows."
        ),
        "risks": [
            "Contractor and unmanaged endpoints",
            "Remote access exposure",
            "Shadow IT and unknown devices",
            "Fragmented investigation data across multiple tools",
        ],
        "value": (
            "Visibility matters because office environments depend on strong correlation between endpoint, "
            "identity, network, and vulnerability context to understand real exposure."
        ),
        "findings": [
            "Unmanaged contractor laptop connected to internal resources",
            "Outdated collaboration room device with incomplete ownership",
            "Unknown printer detected on a trusted office VLAN",
        ],
        "actions": [
            "Validate ownership and policy alignment for unmanaged devices",
            "Correlate endpoint, IAM, and vulnerability signals",
            "Review segmentation and enforcement placement",
            "Push remediation follow-up into ITSM workflows",
        ],
    },
}

# =========================================================
# INTEGRATIONS
# =========================================================

INTEGRATIONS = {
    "EDR": {
        "examples": ["CrowdStrike", "Microsoft Defender", "SentinelOne", "Carbon Black"],
        "description": (
            "Endpoint Detection and Response tools monitor host activity, process behavior, user context, "
            "and response state for managed endpoints."
        ),
        "context": (
            "Adds host telemetry, process chains, logged-in user, device risk, sensor health, "
            "detections, and containment or remediation status."
        ),
        "teams_use_it": [
            "SOC investigates process activity and endpoint detections",
            "Incident response validates severity and containment needs",
            "Endpoint teams review sensor health and remediation state",
        ],
        "architecture": [
            "Managed endpoint generates telemetry",
            "EDR analyzes process activity and host behavior",
            "Findings enrich exposure analysis and investigations",
            "Teams pivot to SIEM, firewall, or ITSM for action",
        ],
        "vendors": {
            "Generic Overview": {
                "summary": "General endpoint telemetry for host activity monitoring and investigation.",
                "data": [
                    "Hostname: ENG-LAPTOP-884",
                    "Logged-in User: jsmith",
                    "OS Version: Windows 11",
                    "Sensor Status: Healthy",
                    "Severity: Medium",
                    "Process Chain: powershell.exe -> rundll32.exe -> suspicious_script.ps1",
                    "Host Isolation: False",
                    "Remediation State: Pending",
                ],
            },
            "CrowdStrike": {
                "summary": "Provides host telemetry, detection metadata, process lineage, and containment status.",
                "data": [
                    "Host: FIN-LAPTOP-210",
                    "Detection ID: 542881",
                    "Severity: Medium",
                    "User: c.garcia",
                    "Process Tree: winword.exe -> powershell.exe -> cmd.exe",
                    "Containment State: Not Isolated",
                    "Sensor Version: 7.04",
                    "Policy: Standard Workstation",
                ],
            },
            "Microsoft Defender": {
                "summary": "Provides endpoint alerts, device risk, exposure insights, and remediation guidance.",
                "data": [
                    "Device: HR-LAPTOP-102",
                    "Device Risk: High",
                    "Exposure Score: 67",
                    "Logged-on Users: m.jordan",
                    "Incident ID: INC-20391",
                    "Alert Category: Suspicious PowerShell",
                    "Remediation Status: In Progress",
                    "Recommendation: Enable attack surface reduction rule",
                ],
            },
            "SentinelOne": {
                "summary": "Provides storyline-based endpoint investigation and mitigation context.",
                "data": [
                    "Endpoint: SALES-LAPTOP-09",
                    "Threat Type: Suspicious Script",
                    "Storyline ID: STL-7752",
                    "Agent State: Connected",
                    "Mitigation Action: Kill Process",
                    "User Context: r.evans",
                    "Policy Group: Remote Endpoints",
                    "Rollback: Not Available",
                ],
            },
            "Carbon Black": {
                "summary": "Provides process telemetry and behavioral hunting context for investigations.",
                "data": [
                    "Endpoint: LAB-WS-44",
                    "Alert Reason: Suspect Lateral Tool",
                    "Process Reputation: Unknown",
                    "Parent Process: wmiprvse.exe",
                    "Child Process: psexec.exe",
                    "Sensor State: Active",
                    "User: local_admin",
                    "Timeline Window: 14:21:08 - 14:23:14",
                ],
            },
        },
    },
    "SIEM": {
        "examples": ["Splunk", "Microsoft Sentinel", "QRadar", "Elastic Security"],
        "description": (
            "Security Information and Event Management platforms aggregate logs, alerts, detections, "
            "and correlation outcomes for centralized monitoring and investigation."
        ),
        "context": (
            "Adds incident history, alert correlation, rule matches, entity pivots, source-destination activity, "
            "and broader cross-tool visibility."
        ),
        "teams_use_it": [
            "SOC correlates alerts from multiple tools",
            "Detection engineers review rule logic and coverage gaps",
            "Analysts pivot between user, device, IP, and alert history",
        ],
        "architecture": [
            "Telemetry flows from multiple tools into SIEM",
            "Correlation connects device, identity, network, and detections",
            "Analysts pivot across entities and incidents",
            "Teams escalate or route action to response workflows",
        ],
        "vendors": {
            "Generic Overview": {
                "summary": "Centralized monitoring and event correlation across security tools.",
                "data": [
                    "Rule: Unusual Authentication + Endpoint Alert Correlation",
                    "Entity: DORM-LAPTOP-447",
                    "User: j.smith",
                    "Source IP: 10.22.18.44",
                    "Destination IP: 10.4.8.90",
                    "Alert Count: 6",
                    "Severity: High",
                    "Case Reference: SOC-2197",
                ],
            },
            "Splunk": {
                "summary": "Searchable log and alert platform used for investigation and correlation.",
                "data": [
                    "Index: security_main",
                    "Host: ENG-LAPTOP-884",
                    "User: jsmith",
                    "Correlation Search: Suspicious Script + New External IP",
                    "Notable Event: Yes",
                    "Risk Score: 42",
                    "Source Type: CrowdStrike:Detection",
                    "Earliest Event: 09:11:07",
                ],
            },
            "Microsoft Sentinel": {
                "summary": "Cloud-native SIEM with incident correlation and entity investigation.",
                "data": [
                    "Incident Name: Multi-stage Endpoint + Identity Anomaly",
                    "Workspace: SOC-Primary",
                    "Entity: alex.morgan@contoso.com",
                    "Device: REMOTE-LAPTOP-31",
                    "Mapped Technique: T1059",
                    "Analytics Rule: Impossible Travel + Endpoint Alert",
                    "Severity: Medium",
                    "Status: Active",
                ],
            },
            "QRadar": {
                "summary": "Offense-level correlation with log and flow analytics.",
                "data": [
                    "Offense ID: 88711",
                    "Magnitude: 7",
                    "Source IP: 10.3.22.8",
                    "Destination IP: 172.16.5.21",
                    "Contributing Log Sources: Firewall, EDR, AD",
                    "Rule Triggered: Excessive Failed Logins + Malware Event",
                    "Flow Count: 13",
                    "Owner: SOC Tier 2",
                ],
            },
            "Elastic Security": {
                "summary": "Indexed detections, timelines, and entity-based analytics.",
                "data": [
                    "Rule: Suspicious Child Process",
                    "Host: LAB-WS-44",
                    "User: local_admin",
                    "Timeline ID: TL-1189",
                    "Severity: High",
                    "Index Pattern: logs-endpoint-*",
                    "Related Event Count: 12",
                    "Case Status: Open",
                ],
            },
        },
    },
    "Firewall": {
        "examples": ["Palo Alto", "Check Point", "Fortinet", "Cisco Secure Firewall"],
        "description": (
            "Firewalls control traffic flows, enforce segmentation, and apply policy decisions "
            "based on network, application, device, or risk context."
        ),
        "context": (
            "Adds policy hits, blocked or allowed traffic, zones, applications, session outcomes, "
            "and segmentation enforcement detail."
        ),
        "teams_use_it": [
            "Network security teams enforce segmentation policies",
            "SOC validates suspicious communications and blocked flows",
            "Operations teams review business impact of restrictions",
        ],
        "architecture": [
            "Visibility platform identifies device or risk context",
            "Firewall consumes context for policy enforcement",
            "Traffic telemetry shows real communication patterns",
            "Teams validate restricted or blocked sessions",
        ],
        "vendors": {
            "Generic Overview": {
                "summary": "General traffic filtering and segmentation enforcement.",
                "data": [
                    "Source Device: Unknown Camera",
                    "Source Zone: IoT Network",
                    "Destination Zone: Internal Apps",
                    "Action: Deny",
                    "Protocol: HTTPS",
                    "Policy Hit: Restricted Device Access",
                    "Session Count: 4",
                    "Last Seen: 10:14:23",
                ],
            },
            "Palo Alto": {
                "summary": "Application-aware firewall enforcement with policy detail.",
                "data": [
                    "Policy Rule: Dorm-IoT-to-Restricted",
                    "Application: ssl",
                    "Source Zone: Student-IoT",
                    "Destination Zone: Academic-Services",
                    "Action: Deny",
                    "Session End Reason: Policy Deny",
                    "User-ID: Unknown",
                    "Device Tag: Unclassified",
                ],
            },
            "Check Point": {
                "summary": "Policy-based segmentation and enforcement with gateway visibility.",
                "data": [
                    "Gateway: GW-East-01",
                    "Rule Number: 87",
                    "Source Object: Unknown_Device_Group",
                    "Destination Object: EMR_Segment",
                    "Service: HTTPS",
                    "Action: Drop",
                    "Log Card: Generated",
                    "Hit Count: 9",
                ],
            },
            "Fortinet": {
                "summary": "Connects device or exposure awareness to firewall policy outcomes.",
                "data": [
                    "Policy ID: 215",
                    "Incoming Interface: wifi-student",
                    "Outgoing Interface: internal-core",
                    "Service: HTTPS",
                    "Action: Deny",
                    "Device Identification: Smart Camera",
                    "Bytes Sent: 0",
                    "Last Policy Match: 11:02:08",
                ],
            },
            "Cisco Secure Firewall": {
                "summary": "Uses visibility data to inform access control and segmentation outcomes.",
                "data": [
                    "Access Control Rule: Restrict Unmanaged Endpoints",
                    "Ingress Zone: VPN-Remote",
                    "Egress Zone: Internal-Apps",
                    "Action: Block",
                    "Application Detected: Unknown TLS",
                    "Connection Events: 3",
                    "Endpoint Identity: Untrusted",
                    "Policy Revision: 22",
                ],
            },
        },
    },
    "NAC": {
        "examples": ["Cisco ISE", "Aruba ClearPass", "FortiNAC"],
        "description": (
            "Network Access Control platforms place devices into the correct network segment, role, "
            "or access policy based on posture, identity, and device type."
        ),
        "context": (
            "Adds switch, port, VLAN, authentication result, role assignment, posture state, "
            "and enforcement action detail."
        ),
        "teams_use_it": [
            "Network teams validate where devices connected and what access they received",
            "Security teams restrict unmanaged assets",
            "Operations teams verify enforcement profile accuracy",
        ],
        "architecture": [
            "Device connects to network",
            "NAC evaluates posture, identity, and classification context",
            "Policy maps device to role, VLAN, or restricted access",
            "Teams verify the outcome and pivot to related workflows",
        ],
        "vendors": {
            "Generic Overview": {
                "summary": "General NAC visibility for admission control and segmentation.",
                "data": [
                    "Switch: SW-DORM-21",
                    "Port: Gi1/0/18",
                    "MAC: 44:38:39:ff:22:01",
                    "VLAN: 220",
                    "Role: Unmanaged Endpoint",
                    "Authentication Result: MAB",
                    "Enforcement Action: Restricted Access",
                    "Session Status: Active",
                ],
            },
            "Cisco ISE": {
                "summary": "Uses device and identity context to drive policy-based access decisions.",
                "data": [
                    "Endpoint: 44:38:39:ff:22:01",
                    "Switch: SW-ACCESS-07",
                    "Policy Set: Student Device Policy",
                    "Auth Method: MAB",
                    "Authorization Result: Limited Access",
                    "SGT: Student-Unmanaged",
                    "Posture Status: Unknown",
                    "Port: Gi1/0/21",
                ],
            },
            "Aruba ClearPass": {
                "summary": "Uses visibility and identity attributes to enforce segmentation and access policy.",
                "data": [
                    "Client MAC: 00:25:96:FF:88:21",
                    "Role Assigned: Guest-IoT",
                    "Enforcement Profile: Restricted-Dorm-Devices",
                    "NAD: DORM-EDGE-04",
                    "Auth Source: Endpoint Repository",
                    "Service Applied: Wireless MAB",
                    "VLAN Assigned: 118",
                    "Session Result: Accepted with Restrictions",
                ],
            },
            "FortiNAC": {
                "summary": "Uses discovered device context to support access control and containment actions.",
                "data": [
                    "Device Name: Unknown-Printer-31",
                    "Host Group: Unclassified Devices",
                    "Location: Building B / Floor 2",
                    "Port: Fa0/11",
                    "Policy Action: Quarantine VLAN",
                    "Scan Result: No Agent",
                    "Access Status: Restricted",
                    "Last Seen: 13:18:54",
                ],
            },
        },
    },
    "Identity / IAM": {
        "examples": ["Active Directory", "Microsoft Entra ID", "Okta"],
        "description": (
            "Identity platforms provide user, account, authentication, lifecycle, and access context "
            "that helps explain who is associated with a device or event."
        ),
        "context": (
            "Adds login activity, MFA status, account state, role, group membership, conditional access, "
            "and sign-in risk."
        ),
        "teams_use_it": [
            "SOC correlates authentication activity to suspicious devices or alerts",
            "IAM teams validate ownership and privilege context",
            "Zero Trust teams strengthen policy decisions using identity signals",
        ],
        "architecture": [
            "Identity source feeds user and auth context into security tools",
            "Authentication events correlate device exposure with account behavior",
            "Teams pivot between user, device, and access activity",
            "Identity findings inform enforcement and remediation",
        ],
        "vendors": {
            "Generic Overview": {
                "summary": "General identity context for ownership, login activity, and access decisions.",
                "data": [
                    "User: j.smith",
                    "Device: STUDENT-LAPTOP-447",
                    "Domain: campus.local",
                    "Authentication Type: Kerberos",
                    "Source IP: 10.22.18.44",
                    "Login Time: 08:44:13",
                    "Account Status: Enabled",
                    "Password Last Changed: 14 days ago",
                ],
            },
            "Active Directory": {
                "summary": "Provides directory-based identity, device ownership, and group membership context.",
                "data": [
                    "User: j.smith",
                    "Device: DORM-LAPTOP-447",
                    "Domain: campus.local",
                    "OU: Student Devices",
                    "Authentication Event: Kerberos",
                    "Source IP: 10.22.18.44",
                    "Groups: Domain Users, Student Access, Dorm Network Users",
                    "Account Status: Enabled",
                ],
            },
            "Microsoft Entra ID": {
                "summary": "Provides cloud identity, sign-in risk, and conditional access context.",
                "data": [
                    "User: alex.morgan@contoso.com",
                    "Sign-in Risk: Medium",
                    "MFA Status: Registered",
                    "Conditional Access Result: Success",
                    "Device Compliance: Unknown",
                    "App Accessed: Microsoft 365",
                    "Source Country: United States",
                    "User Role: Standard User",
                ],
            },
            "Okta": {
                "summary": "Provides SSO, MFA, app assignment, and lifecycle context.",
                "data": [
                    "User: contractor01",
                    "Status: Active",
                    "Last Login: 07:13:21",
                    "MFA Enrollment: Partial",
                    "Assigned Apps: VPN, Salesforce, Slack",
                    "Group Membership: Contractors, Remote Users",
                    "Policy Outcome: Step-up MFA Required",
                    "Device Trust: Unknown",
                ],
            },
        },
    },
    "Vulnerability Management": {
        "examples": ["Tenable", "Qualys", "Rapid7"],
        "description": (
            "Vulnerability management platforms enrich asset records with findings, severity, patch gaps, "
            "remediation context, and exposure prioritization."
        ),
        "context": (
            "Adds CVEs, severity, scan timestamps, missing patches, vulnerability age, asset criticality, "
            "and exposed services."
        ),
        "teams_use_it": [
            "Security teams prioritize remediation based on exposure",
            "Operations teams validate patching and ownership",
            "Analysts correlate exposure with device criticality and business impact",
        ],
        "architecture": [
            "Asset is identified in the environment",
            "Vulnerability platform enriches it with findings and severity",
            "Exposure is prioritized with ownership or criticality context",
            "Teams route action to remediation workflows",
        ],
        "vendors": {
            "Generic Overview": {
                "summary": "General vulnerability context for exposure and remediation prioritization.",
                "data": [
                    "Asset: APP-SERVER-22",
                    "Critical Findings: 3",
                    "Top CVE: CVE-2025-9988",
                    "CVSS: 9.1",
                    "Patch Status: Missing",
                    "Exposed Service: HTTPS",
                    "Last Scan: 2026-03-12 02:14",
                    "Vulnerability Age: 47 days",
                ],
            },
            "Tenable": {
                "summary": "Provides plugin-based findings, severity, patch gaps, and exposure context.",
                "data": [
                    "Asset: ENG-LAPTOP-884",
                    "Plugin ID: 181245",
                    "CVE: CVE-2025-9988",
                    "Severity: Critical",
                    "Patch Available: Yes",
                    "Last Authenticated Scan: 2026-03-13 01:05",
                    "Exploit Available: Possible",
                    "Asset Criticality Rating: High",
                ],
            },
            "Qualys": {
                "summary": "Provides vulnerability findings, asset tags, and patch status context.",
                "data": [
                    "Host: HR-LAPTOP-102",
                    "QID: 376157",
                    "CVE Count: 12",
                    "Top Severity: 5",
                    "Patchable: Yes",
                    "Cloud Agent Status: Active",
                    "Asset Tags: Finance, Remote User",
                    "Last Detection Update: 2026-03-14 09:44",
                ],
            },
            "Rapid7": {
                "summary": "Provides exposure prioritization and remediation project context.",
                "data": [
                    "Asset: REMOTE-LAPTOP-31",
                    "Risk Score: 812",
                    "Critical Vulnerabilities: 2",
                    "Most Exploitable Finding: CVE-2025-8871",
                    "Solution: Update OpenSSL package",
                    "Last Scan Engine: Cloud Collector 3",
                    "Site: Remote Workforce",
                    "Remediation Project: Remote Endpoint Patch Sprint",
                ],
            },
        },
    },
    "Threat Intelligence": {
        "examples": ["Anomali", "Recorded Future", "VirusTotal"],
        "description": (
            "Threat intelligence platforms enrich indicators and observables with reputation, campaign, "
            "malware, and confidence context."
        ),
        "context": (
            "Adds reputation, confidence, malware associations, campaign detail, risk scoring, "
            "and threat category context for observables."
        ),
        "teams_use_it": [
            "Threat intel teams enrich indicators before escalation",
            "SOC validates whether observables are known bad or suspicious",
            "Incident response uses intel to prioritize containment decisions",
        ],
        "architecture": [
            "Observable is identified in a workflow",
            "Threat intelligence enriches it with reputation and context",
            "Teams correlate with SIEM, EDR, or network data",
            "Intel guides prioritization and response direction",
        ],
        "vendors": {
            "Generic Overview": {
                "summary": "General indicator enrichment for reputation and prioritization.",
                "data": [
                    "Observable: 185.244.25.91",
                    "Type: IP Address",
                    "Confidence: 82",
                    "Reputation: Malicious",
                    "Associated Campaign: Credential Theft Infrastructure",
                    "Related Malware: StealerX",
                    "First Seen: 2026-02-18",
                    "Last Updated: 2026-03-10",
                ],
            },
            "Anomali": {
                "summary": "Provides IOC enrichment, campaign context, and downstream prioritization.",
                "data": [
                    "Indicator: suspicious-login-update[.]com",
                    "Feed Source: Premium Intel Feed",
                    "Indicator Type: Domain",
                    "Confidence: High",
                    "Campaign: Phishing Infrastructure Set B",
                    "TLP: Amber",
                    "Related Observables: 4",
                    "Threat Type: Credential Phishing",
                ],
            },
            "Recorded Future": {
                "summary": "Provides intelligence-based risk scoring and entity analysis.",
                "data": [
                    "Entity: 185.244.25.91",
                    "Risk Score: 91",
                    "Threat List Presence: Yes",
                    "Related Malware: RedLine",
                    "Threat Actor Mention: Possible",
                    "Reference Count: 12",
                    "Category: C2 Infrastructure",
                    "Priority: High",
                ],
            },
            "VirusTotal": {
                "summary": "Provides multi-engine reputation and artifact relationship context.",
                "data": [
                    "Hash: 7f8a1e4c9d11...",
                    "Detection Count: 24/71",
                    "Artifact Type: File",
                    "Behavior Tag: Downloader",
                    "Related Domains: 3",
                    "Network Contacted: 185.244.25.91",
                    "First Submission: 2026-03-08",
                    "Community Score: -5",
                ],
            },
        },
    },
}

DEFAULT_SCENARIO = "Medical / Healthcare"
DEFAULT_INTEGRATION = "EDR"
DEFAULT_VENDOR = "Generic Overview"

# =========================================================
# HELPERS
# =========================================================

def bullet_list(items):
    return "\n".join(f"- {item}" for item in items)

def get_vendor_choices(integration_type):
    if integration_type in INTEGRATIONS:
        return list(INTEGRATIONS[integration_type]["vendors"].keys())
    return ["Generic Overview"]

def build_example_block(items):
    return "\n".join(items)

def build_scenario_specific_value(scenario_name, integration_type, vendor_name):
    if scenario_name == "Medical / Healthcare":
        return (
            f"In a healthcare environment, the {integration_type} integration using {vendor_name} helps security teams "
            "understand whether activity is tied to a managed workstation, a clinical workflow, an unmanaged medical device, "
            "or a communication path that could affect sensitive systems."
        )
    if scenario_name == "Operational Technology / IoT":
        return (
            f"In an OT / IoT environment, the {integration_type} integration using {vendor_name} adds context that is "
            "especially valuable when devices cannot run agents and teams must rely on network visibility, policy placement, "
            "or external telemetry to understand risk."
        )
    if scenario_name == "School / Education":
        return (
            f"In an education environment, the {integration_type} integration using {vendor_name} helps teams deal with "
            "rapid device turnover, shared infrastructure, dorm networks, and uncertain ownership across large user populations."
        )
    return (
        f"In a corporate office environment, the {integration_type} integration using {vendor_name} helps correlate endpoint, "
        "identity, network, and vulnerability signals so teams can move faster from visibility to triage and remediation."
    )

def build_architecture_flow(integration_type):
    flows = {
        "EDR": [
            "Device appears on network",
            "Managed endpoint generates host telemetry",
            "EDR identifies process activity and detections",
            "Exposure is correlated with device and user context",
            "Security team investigates or responds",
        ],
        "SIEM": [
            "Device or alert is observed",
            "Telemetry flows from multiple tools into SIEM",
            "Correlation rules connect related events",
            "Analyst pivots across user, device, and IP context",
            "Incident is triaged or escalated",
        ],
        "Firewall": [
            "Device communicates across network segments",
            "Firewall evaluates policy and zone context",
            "Traffic is allowed, denied, or restricted",
            "Security team reviews session and policy outcomes",
            "Segmentation is adjusted if needed",
        ],
        "NAC": [
            "Device appears on network",
            "NAC identifies posture, role, or authentication status",
            "Device is mapped to access policy or VLAN",
            "Security team validates access level",
            "Unmanaged or risky assets are restricted",
        ],
        "Identity / IAM": [
            "User attempts access or authentication",
            "Identity platform records login and policy outcome",
            "Device and account activity are correlated",
            "Security team reviews ownership and sign-in risk",
            "Access decisions or follow-up actions are taken",
        ],
        "Vulnerability Management": [
            "Asset is identified in the environment",
            "Scanner or agent enriches it with findings",
            "Severity and exposure are prioritized",
            "Ownership and remediation path are identified",
            "Team schedules remediation or containment",
        ],
        "Threat Intelligence": [
            "Observable is identified in an alert or workflow",
            "Threat intel enriches indicator with reputation and context",
            "Related campaigns or malware associations are reviewed",
            "Security team determines priority and scope",
            "Investigation or containment is escalated",
        ],
    }
    return flows.get(integration_type, ["Device appears on network", "Security team investigates context"])

def build_business_outcomes(scenario_name, integration_type):
    base = [
        "Improve asset visibility across managed and unmanaged environments",
        "Reduce investigation time by enriching devices with contextual telemetry",
        "Support faster triage and prioritization for security teams",
        "Strengthen ownership, governance, and remediation workflows",
    ]

    scenario_specific = {
        "Medical / Healthcare": "Reduce operational and patient-care risk through stronger visibility near clinical systems",
        "Operational Technology / IoT": "Improve awareness of unmanaged industrial assets and reduce disruption risk",
        "School / Education": "Improve classification and ownership validation across high-churn device environments",
        "Corporate Office": "Strengthen endpoint, identity, and network correlation across distributed users and devices",
    }

    integration_specific = {
        "EDR": "Improve managed endpoint investigation and host-based threat response",
        "SIEM": "Centralize alert correlation and improve cross-tool investigation speed",
        "Firewall": "Support segmentation decisions and reduce lateral movement opportunities",
        "NAC": "Improve access control and restrict unmanaged or non-compliant devices",
        "Identity / IAM": "Improve user-to-device attribution and access policy decisions",
        "Vulnerability Management": "Prioritize remediation using exposure and severity context",
        "Threat Intelligence": "Improve prioritization of suspicious observables with reputation and campaign context",
    }

    outcomes = base.copy()
    outcomes.append(scenario_specific.get(scenario_name, "Improve visibility and investigation quality"))
    outcomes.append(integration_specific.get(integration_type, "Improve security operations efficiency"))
    return outcomes

def build_analysis(scenario_name, integration_type, vendor_name):
    scenario = SCENARIOS.get(scenario_name, SCENARIOS[DEFAULT_SCENARIO])
    integration = INTEGRATIONS.get(integration_type, INTEGRATIONS[DEFAULT_INTEGRATION])

    if vendor_name not in integration["vendors"]:
        vendor_name = "Generic Overview"

    vendor = integration["vendors"][vendor_name]
    examples = ", ".join(integration["examples"])
    architecture_flow = build_architecture_flow(integration_type)
    business_outcomes = build_business_outcomes(scenario_name, integration_type)

    return (
        f"# Integration Analysis\n\n"
        f"**Scenario:** {scenario_name}  \n"
        f"**Integration Type:** {integration_type}  \n"
        f"**Vendor:** {vendor_name}\n\n"
        f"## Scenario Summary\n\n"
        f"{scenario['summary']}\n\n"
        f"## Key Risks in This Environment\n\n"
        f"{bullet_list(scenario['risks'])}\n\n"
        f"## Why Visibility Matters Here\n\n"
        f"{scenario['value']}\n\n"
        f"## Example Findings\n\n"
        f"{bullet_list(scenario['findings'])}\n\n"
        f"## Recommended Actions\n\n"
        f"{bullet_list(scenario['actions'])}\n\n"
        f"---\n\n"
        f"## Integration Overview\n\n"
        f"- **Example Vendors:** {examples}\n"
        f"- **What It Does:** {integration['description']}\n"
        f"- **What Context It Provides:** {integration['context']}\n\n"
        f"## Vendor-Specific Context\n\n"
        f"{vendor['summary']}\n\n"
        f"## Scenario-Specific Value\n\n"
        f"{build_scenario_specific_value(scenario_name, integration_type, vendor_name)}\n\n"
        f"## Example Data / Context Provided\n\n"
        f"```text\n"
        f"{build_example_block(vendor['data'])}\n"
        f"```\n\n"
        f"## How Security Teams Use This\n\n"
        f"{bullet_list(integration['teams_use_it'])}\n\n"
        f"## Security Architecture Map\n\n"
        f"{bullet_list(integration['architecture'])}\n\n"
        f"## Example Workflow\n\n"
        f"{bullet_list(architecture_flow)}\n\n"
        f"## Business Outcome Mapping\n\n"
        f"{bullet_list(business_outcomes)}\n"
    )

def initialize():
    return build_analysis(DEFAULT_SCENARIO, DEFAULT_INTEGRATION, DEFAULT_VENDOR)

def integration_changed(scenario_name, integration_type):
    vendor_choices = get_vendor_choices(integration_type)
    vendor_value = "Generic Overview"
    analysis = build_analysis(scenario_name, integration_type, vendor_value)
    return gr.update(choices=vendor_choices, value=vendor_value), analysis

def refresh_output(scenario_name, integration_type, vendor_name):
    return build_analysis(scenario_name, integration_type, vendor_name)

# =========================================================
# UI
# =========================================================

CSS = """
body, .gradio-container {
    background: linear-gradient(180deg, #120d00 0%, #1b1400 100%) !important;
    color: #fdf4d2 !important;
    font-family: Inter, Arial, sans-serif;
}

.gradio-container {
    max-width: 1450px !important;
    margin: 0 auto !important;
    padding-top: 18px !important;
    padding-bottom: 22px !important;
}

.hero {
    background: linear-gradient(135deg, #241b00 0%, #171100 100%);
    border: 1px solid #8a6b00;
    border-radius: 18px;
    padding: 20px 22px;
    margin-bottom: 14px;
    box-shadow: 0 8px 28px rgba(0, 0, 0, 0.30);
}

.hero h1 {
    margin: 0 0 6px 0;
    font-size: 34px;
    color: #d7aa12;
    font-weight: 800;
    letter-spacing: -0.02em;
}

.hero p {
    margin: 0;
    color: #f4e6b0;
    font-size: 14px;
}

.controls-wrap {
    background: linear-gradient(135deg, #2a2100 0%, #1c1500 100%) !important;
    border: 1px solid #8a6b00;
    border-radius: 18px;
    padding: 14px;
    margin-bottom: 14px;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.18);
}

.control-title {
    color: #d7aa12;
    font-size: 12px;
    font-weight: 900;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 6px;
}

.analysis-panel {
    background: linear-gradient(180deg, #231b00 0%, #171100 100%) !important;
    border: 1px solid #a67d00 !important;
    border-radius: 18px !important;
    padding: 22px !important;
    min-height: 760px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.22);
}

.markdown, .prose, .markdown p, .markdown li, .markdown strong,
.prose p, .prose li, .prose strong {
    color: #fdf4d2 !important;
    font-size: 15px !important;
    line-height: 1.65 !important;
}

.markdown h1, .markdown h2, .markdown h3, .markdown h4,
.prose h1, .prose h2, .prose h3, .prose h4 {
    color: #d7aa12 !important;
}

.markdown hr, .prose hr {
    border-color: #6b5200 !important;
}

label {
    color: #f4df96 !important;
    font-weight: 700 !important;
    font-size: 14px !important;
}

.gradio-dropdown,
.gr-text-input,
.gr-textbox,
.gr-box,
.gr-form,
.gr-group {
    border-radius: 14px !important;
}

.gradio-dropdown label,
.gradio-dropdown span,
.gradio-dropdown div,
.gradio-dropdown input {
    color: #f5d66f !important;
}

.gradio-container .gr-input,
.gradio-container .gr-box,
.gradio-container .gr-form,
.gradio-container select,
.gradio-container input,
.gradio-container textarea {
    background: #2a2100 !important;
    color: #fdf4d2 !important;
    border: 1px solid #8a6b00 !important;
}

.gradio-container .wrap,
.gradio-container .block {
    border-radius: 14px !important;
}

footer {
    display: none !important;
}
"""

with gr.Blocks(css=CSS) as demo:
    gr.HTML(
        f"""
        <div class="hero">
            <h1>{APP_TITLE}</h1>
            <p>{APP_SUBTITLE}</p>
        </div>
        """
    )

    with gr.Group(elem_classes=["controls-wrap"]):
        with gr.Row():
            with gr.Column():
                gr.HTML('<div class="control-title">Scenario</div>')
                scenario_dropdown = gr.Dropdown(
                    label="Scenario",
                    choices=list(SCENARIOS.keys()),
                    value=DEFAULT_SCENARIO,
                    interactive=True,
                )

            with gr.Column():
                gr.HTML('<div class="control-title">Integration Type</div>')
                integration_dropdown = gr.Dropdown(
                    label="Integration Type",
                    choices=list(INTEGRATIONS.keys()),
                    value=DEFAULT_INTEGRATION,
                    interactive=True,
                )

            with gr.Column():
                gr.HTML('<div class="control-title">Integration Vendor</div>')
                vendor_dropdown = gr.Dropdown(
                    label="Integration Vendor",
                    choices=get_vendor_choices(DEFAULT_INTEGRATION),
                    value=DEFAULT_VENDOR,
                    interactive=True,
                )

    analysis_output = gr.Markdown(elem_classes=["analysis-panel"])

    demo.load(
        fn=initialize,
        outputs=analysis_output,
    )

    integration_dropdown.change(
        fn=integration_changed,
        inputs=[scenario_dropdown, integration_dropdown],
        outputs=[vendor_dropdown, analysis_output],
    )

    scenario_dropdown.change(
        fn=refresh_output,
        inputs=[scenario_dropdown, integration_dropdown, vendor_dropdown],
        outputs=analysis_output,
    )

    vendor_dropdown.change(
        fn=refresh_output,
        inputs=[scenario_dropdown, integration_dropdown, vendor_dropdown],
        outputs=analysis_output,
    )

if __name__ == "__main__":
    demo.launch()
