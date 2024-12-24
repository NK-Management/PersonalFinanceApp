from flask import Blueprint, request, jsonify
from services.expense_tracking_service.app.services.jar_service import JarService

bp = Blueprint('jars', __name__)

@bp.route('/', methods=['POST'])
def create_jar():
    data = request.get_json()
    result = JarService.create_jar(data)
    return jsonify(result), 201

@bp.route('/', methods=['GET'])
def get_all_jars():
    jars = JarService.get_all_jars()
    return jsonify(jars)

@bp.route('/<int:id>', methods=['PUT'])
def update_jar(id):
    data = request.get_json()
    result = JarService.update_jar(id, data)
    return jsonify(result)

@bp.route('/<int:id>', methods=['DELETE'])
def delete_jar(id):
    result = JarService.delete_jar(id)
    return jsonify(result)
