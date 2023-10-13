from flask import request

application = {
    "destination_port": 53,
    "flow_duration": 500,
    "total_length_of_fwd_packets": 80,
    "total_length_of_bwd_packets": 50,
    "fwd_packet_length_max": 40,
    "fwd_packet_length_min": 40,
    "bwd_packet_length_min": 0,
    "flow_bytes_s": 3500,
    "flow_packets_s": 35,
    "flow_iat_mean": 4,
    "flow_iat_min": 4,
    "fwd_iat_max": 4,
    "bwd_iat_max": 5,
    "bwd_iat_min": 2,
    "fwd_psh_flags": 1,
    "fwd_urg_flags": 0,
    "fwd_header_length": 2,
    "bwd_packets_s": 45,
    "min_packet_length": 4,
    "fin_flag_count": 0,
    "syn_flag_count": 0,
    "rst_flag_count": 1,
    "psh_flag_count": 1,
    "ack_flag_count": 0,
    "urg_flag_count": 0,
    "cwe_flag_count": 1,
    "ece_flag_count": 0,
    "down_up_ratio": 8,
    "average_packet_size": 3000,
    "init_win_bytes_forward": 400,
    "init_win_bytes_backward": 1,
    "active_max": 0,
    "active_min": 0,
    "idle_std": 1,

}


# Location of my server
url = "http://127.0.0.1:8989/predict"

# Send request
resp = requests.post(url, json=application)

# Print result
print(resp.json())
