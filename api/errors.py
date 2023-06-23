from flask import Blueprint, jsonify
import traceback
import logging
log = logging.getLogger(__name__)

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(404)
def not_found_error(error):
    return jsonify({'message': 'resource not found'}), 404


@errors.app_errorhandler(500)
def internal_error(e):
    log.error(traceback.format_exc())
    lines = traceback.format_exception(type(e), e, e.__traceback__)
    return jsonify({'message':'internal server error', "error": lines}), 500


@errors.app_errorhandler(Exception)
def default_handler(e):
    log.error(traceback.format_exc())
    return jsonify({'message': 'internal server error', "error": str(e), "stack": traceback.format_exception(type(e), e, e.__traceback__)}), 500
