import os
import json
import pandas as pd
from flask import Response, jsonify

DATA_FILE = os.getenv("DATA_FILE", "data/services_data.json")

def export_to_csv(df):
    csv_data = df.to_csv(index=False)
    return Response(csv_data, mimetype='text/csv')

def services_to_csv():
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        
        services = data.get("services", [])
        
        df = pd.DataFrame(services, columns=["name", "status", "last_incident_timestamp"])
        
        if "last_incident_timestamp" not in df.columns:
            df["last_incident_timestamp"] = "N/A"
        
        return export_to_csv(df)
    except FileNotFoundError:
        return jsonify({"error": "Datos no encontrados."}), 500

def incidents_per_service_to_csv():
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        
        services = data.get("services", [])
        
        data_for_csv = [
            {"name": service["name"], "has_incident": service.get("last_incident_timestamp") is not None}
            for service in services
        ]
        
        df = pd.DataFrame(data_for_csv)
        
        return export_to_csv(df)
    except FileNotFoundError:
        return jsonify({"error": "Datos no encontrados."}), 500

def incidents_by_service_and_status_to_csv():
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        
        services = data.get("services", [])
        
        data_for_csv = []
        for service in services:
            name = service["name"]
            status = service.get("status", "unknown")
            incidents = 1 if service.get("last_incident_timestamp") else 0
            data_for_csv.append({"name": name, "status": status, "incidents": incidents})
        
        df = pd.DataFrame(data_for_csv)
        
        return export_to_csv(df)
    except FileNotFoundError:
        return jsonify({"error": "Datos no encontrados."}), 500

def teams_and_services_to_csv():
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

        data_for_csv = []
        for team_name, info in teams_data.items():
            for service in info["services"]:
                data_for_csv.append({"team": team_name, "service": service})

        df = pd.DataFrame(data_for_csv)
        
        return export_to_csv(df)
    except FileNotFoundError:
        return jsonify({"error": "Datos no encontrados."}), 500


