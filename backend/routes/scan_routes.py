from flask import Blueprint, request, jsonify
from scanner.sqli import detect_sqli
from scanner.xss import detect_xss
from scanner.auth_bypass import detect_auth_bypass

scan_bp = Blueprint("scan", __name__)

@scan_bp.route("/scan", methods=["POST"])
def scan():
    data = request.get_json()
    url = data.get("url")

    results = {}

    results["sqli"] = detect_sqli(url)
    results["xss"] = detect_xss(url)
    results["auth_bypass"] = detect_auth_bypass(url)

    return jsonify(results)