import numpy as np
import pandas as pd
import os
import utils as ld # <-- import whole utils module

# Absolute path to Json_data folder
script_dir = os.path.dirname(os.path.abspath(__file__))
json_dir = os.path.join(script_dir, "Json_data")

files = os.listdir(json_dir)
print("Files: ")
print(files)
print("##########################")
# file_list = [ 
#     "ticket_002_security_breach.json",
#     "ticket_003_network_outage.json",
#     "ticket_004_email_spam.json",
#     "ticket_005_software_license.json",
#     "ticket_006_backup_corruption.json",
#     "ticket_006_backup_corruption.json",
#     "ticket_007_wireless_security.json",
#     "ticket_008_database_performance.json",
#     "ticket_009_phone_system_failure.json",
#     "ticket_010_file_server_crash.json",
#     "ticket_011_remote_desktop_issues.json",
#     "ticket_012_antivirus_false_positive.json",
#     "ticket_013_cloud_sync_issues.json",
#     "ticket_014_printer_driver_conflict.json",
#     "ticket_015_website_downtime.json",
#     "ticket_016_mobile_device_management.json",
#     "ticket_017_network_segmentation.json",
#     "ticket_018_data_migration.json",
#     "ticket_019_security_patch_deployment.json",
#     "ticket_020_disaster_recovery_test.json"
# ]

try:
    df = ld.load_data(files)
    print(df)
    print("Columns: ")
    print(df.columns)
except Exception as e:
    print(f"[Main Error] Failed to load data: {e}")
    df = pd.DataFrame()  # fallback to empty DataFrame

# Only try to add cols if DataFrame is not empty
if not df.empty:
    df = ld.add_cols(df)
    print(df)
    print("Columns: ")
    print(df.columns)
else:
    print("[Warning] No data available to process.")
