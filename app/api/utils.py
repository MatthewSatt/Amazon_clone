from flask import jsonify, request


def error(message, status=400, field='form'):
    return jsonify(errors={field: [message]}), status


def json_body():
    return request.get_json(silent=True) or {}


def form_errors(form):
    """WTForms errors as {field: [messages]}"""
    return jsonify(errors=form.errors), 400


def as_int(value):
    """int(value), or None if it isn't a clean integer"""
    if isinstance(value, bool):
        return None
    try:
        return int(value)
    except (TypeError, ValueError):
        return None
