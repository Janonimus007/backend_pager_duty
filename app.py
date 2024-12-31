from flask import Flask, jsonify,Blueprint
from services.fetch_data import fetch_and_set_data 
from controllers.services_controller import (
    get_services,
    get_incidents_per_service,
    get_incidents_by_service_and_status,
    get_teams_and_services,
    get_escalation_policies
)
from controllers.services_controller_csv import (
    services_to_csv,
    incidents_per_service_to_csv,
    incidents_by_service_and_status_to_csv,
    teams_and_services_to_csv
)

app = Flask(__name__)

# Routes
app.route('/services', methods=['GET'])(get_services)
app.route('/services/incidents', methods=['GET'])(get_incidents_per_service)
app.route('/services/incidents/status', methods=['GET'])(get_incidents_by_service_and_status)
app.route('/teams/services', methods=['GET'])(get_teams_and_services)
app.route('/escalation-policies', methods=['GET'])(get_escalation_policies)

# Routes csv
@app.route('/services/csv', methods=['GET'])
def download_services_csv():
    return services_to_csv()

@app.route('/services/incidents/csv', methods=['GET'])
def download_incidents_per_service_csv():
    return incidents_per_service_to_csv()

@app.route('/services/incidents/status/csv', methods=['GET'])
def download_incidents_by_service_and_status_csv():
    return incidents_by_service_and_status_to_csv()

@app.route('/teams/services/csv', methods=['GET'])
def download_teams_and_services_csv():
    return teams_and_services_to_csv()
    
if __name__ == '__main__':
    fetch_and_set_data()
    app.run(debug=True)
