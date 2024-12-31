import os
import json
from flask import jsonify

DATA_FILE = os.getenv("DATA_FILE", "data/services_data.json")

def get_services():
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "Datos no encontrados."}), 500

def get_incidents_per_service():
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        
        incidents_data = {
            service["name"]: service.get("last_incident_timestamp") is not None
            for service in data.get("services", [])
        }
        
        return jsonify(incidents_data)
    except FileNotFoundError:
        return jsonify({"error": "Datos no encontrados. Asegúrate de haber llamado a la API correctamente."}), 500

def get_incidents_by_service_and_status():
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        
        services_status_data = {}
        for service in data.get("services", []):
            service_name = service["name"]
            status = service.get("status", "unknown")  
            has_incident = service.get("last_incident_timestamp") is not None  
            
            if service_name not in services_status_data:
                services_status_data[service_name] = {"status": status, "incidents": 0}
            
            if has_incident:
                services_status_data[service_name]["incidents"] += 1 
        
        return jsonify(services_status_data)
    except FileNotFoundError:
        return jsonify({"error": "Datos no encontrados. Asegúrate de haber llamado a la API correctamente."}), 500

def get_teams_and_services():
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        
        teams_data = {}

        for service in data.get("services", []):
            teams = service.get("teams", [])
            for team in teams:
                team_name = team["summary"]  
                service_name = service["name"]  

                if team_name not in teams_data:
                    teams_data[team_name] = {"services": []}
                
                teams_data[team_name]["services"].append(service_name)

        for team_name, info in teams_data.items():
            info["service_count"] = len(info["services"])

        return jsonify(teams_data)
    except FileNotFoundError:
        return jsonify({"error": "Datos no encontrados. Asegúrate de haber llamado a la API correctamente."}), 500


def get_escalation_policies():
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        
        escalation_policies = {}

        for service in data.get("services", []):
            escalation_policy = service.get("escalation_policy", {})
            if escalation_policy:
                escalation_id = escalation_policy["id"]
                escalation_summary = escalation_policy["summary"]
                service_name = service["name"]
                teams = [team["summary"] for team in service.get("teams", [])]

                if escalation_id not in escalation_policies:
                    escalation_policies[escalation_id] = {
                        "summary": escalation_summary,
                        "services": [],
                        "teams": set()
                    }

                escalation_policies[escalation_id]["services"].append(service_name)
                escalation_policies[escalation_id]["teams"].update(teams)

        for policy in escalation_policies.values():
            policy["teams"] = list(policy["teams"])
            policy["service_count"] = len(policy["services"])
            policy["team_count"] = len(policy["teams"])

        return jsonify(escalation_policies)
    except FileNotFoundError:
        return jsonify({"error": "Datos no encontrados. Asegúrate de haber llamado a la API correctamente."}), 500