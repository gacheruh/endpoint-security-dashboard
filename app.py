import streamlit as st
import pandas as pd
from utils.security_analytics import load_security_data, get_antivirus_summary, get_incident_summary

st.set_page_config(
    page_title="Endpoint Security & Phishing Awareness Dashboard",
    page_icon="🛡️",
    layout="wide"
)

st.title("Endpoint Security & Phishing Awareness Dashboard")
st.markdown("Monitoring endpoint protection statuses, antivirus health checks, and reported security incidents across UAF-Africa's virtual workspaces.")

df = load_security_data()

tab1, tab2, tab3 = st.tabs(["Security Posture Overview", "Antivirus & Health Status", "Phishing & Incident Response"])

with tab1:
    st.header("Virtual Organization Security Metrics")
    if not df.empty:
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Monitored Endpoints", len(df))
        with col2:
            av_issues = len(df[df['antivirus_status'] != 'Active'])
            st.metric("AV Deficiencies / Disabled", av_issues, delta_color="inverse")
        with col3:
            incidents = len(df[df['incident_type'] != 'None'])
            st.metric("Reported Security Incidents", incidents)
        with col4:
            action_req = len(df[df['remediation_status'] == 'Action Required'])
            st.metric("Pending Remediation", action_req, delta_color="inverse")
            
        st.subheader("Endpoint Inventory & Status Log")
        st.dataframe(df, use_container_width=True)
    else:
        st.warning("No security data found.")

with tab2:
    st.header("Antivirus & Health Check Status")
    st.markdown("Tracking endpoint agent protection status across regional offices.")
    if not df.empty:
        av_counts = get_antivirus_summary(df)
        st.bar_chart(av_counts)
        
        st.subheader("Endpoints Requiring Immediate AV Attention")
        unhealthy_df = df[df['antivirus_status'] != 'Active']
        if not unhealthy_df.empty:
            st.dataframe(unhealthy_df[['device_id', 'user_email', 'office_location', 'antivirus_status', 'last_scan_date']], use_container_width=True)
        else:
            st.success("All monitored endpoints have active antivirus protection.")
    else:
        st.warning("No data available.")

with tab3:
    st.header("Phishing & Security Incident Tracker")
    st.markdown("Logging phishing awareness reports, unauthorized access attempts, and recommended remediation steps.")
    if not df.empty:
        inc_df = df[df['incident_type'] != 'None']
        
        for index, row in inc_df.iterrows():
            with st.expander(f"[{row['severity']}] {row['incident_type']} - {row['user_email']} ({row['office_location']})"):
                st.write(f"**Device ID:** {row['device_id']}")
                st.write(f"**Description:** {row['description']}")
                st.write(f"**Status:** {row['remediation_status']}")
                
                # Recommended remediation steps based on incident type (safeguarded with str())
                incident = str(row['incident_type'])
                if "Phishing" in incident:
                    st.info("**Recommended Remediation:** Revoke active user sessions, force Microsoft 365 password reset, and review email forwarding rules.")
                elif "Unauthorized Access" in incident:
                    st.warning("**Recommended Remediation:** Block originating IP address in firewall/security group, review IAM access logs, and notify security lead.")
                else:
                    st.success("**Recommended Remediation:** Verify quarantine status and confirm system file integrity.")
    else:
        st.warning("No security incidents reported.")