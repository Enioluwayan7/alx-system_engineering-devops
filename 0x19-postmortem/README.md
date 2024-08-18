Postmortem: Outage of CryptoPulse Website

Issue Summary:

- Duration: The outage occurred on August 20, 2024, from 14:00 to 15:45 GMT (1 hour 45 minutes).
- Impact: The CryptoPulse website was completely inaccessible during this period. Users experienced a "504 Gateway Timeout" error when trying to access the site. Approximately 85% of the user base was affected, leading to a significant drop in user engagement and transactions during the outage.
- Root Cause: The root cause was a misconfiguration in the Nginx server that led to an overload of incoming requests, causing the server to become unresponsive.

Timeline:

- 14:00 GMT: Issue detected by monitoring alerts indicating a spike in server response times.
- 14:05 GMT: An engineer noticed a surge in error logs and flagged the issue as a potential outage.
- 14:10 GMT: Initial investigation focused on the database server, suspecting a bottleneck in queries.
- 14:20 GMT: Database performance metrics were normal, leading the team to inspect the Nginx server configuration.
- 14:30 GMT: Misleading investigation into network latency, which was later ruled out as the cause.
- 14:40 GMT: Incident escalated to the DevOps team, who identified the misconfiguration in Nginx.
- 15:00 GMT: Nginx configuration was corrected, and the server was restarted.
- 15:15 GMT: Website accessibility restored, but the site remained under observation for any further issues.
- 15:45 GMT: Monitoring confirmed that the site was stable, and the incident was marked as resolved.

Root Cause and Resolution:

- Root Cause: The issue stemmed from a misconfigured Nginx server, where the worker_processes directive was set too low, limiting the number of concurrent connections the server could handle. As user traffic increased, the limited number of worker processes became overwhelmed, leading to the server's inability to process incoming requests, resulting in a 504 Gateway Timeout error.
- Resolution: The Nginx configuration was adjusted by increasing the worker_processes directive to a value that could handle the current user load. Additionally, the server was restarted to apply the changes. This resolved the issue, restoring normal operation to the website.

Corrective and Preventative Measures:

- Improvements/Fixes:
  - Nginx Configuration Review: Conduct a comprehensive review of the Nginx configuration to ensure all settings are optimized for current traffic levels.
  - Capacity Planning: Implement regular capacity planning to anticipate future traffic spikes and adjust server configurations accordingly.
  - Enhanced Monitoring: Set up more granular monitoring for Nginx performance, including real-time alerts for worker process saturation.
  - Documentation: Improve documentation on server configuration to prevent similar misconfigurations in the future.

- Tasks:
  - Patch Nginx server configuration.
  - Add monitoring on server memory and worker processes.
  - Conduct a load test on the website to validate the new configuration.
  - Schedule regular reviews of server configurations and performance metrics.

This postmortem provides a detailed account of the CryptoPulse website outage, addressing the root cause, resolution, and steps for future prevention to ensure a more resilient system.

