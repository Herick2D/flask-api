from flask import Blueprint, jsonify, request, Response
from app import db
from app.models import User
from typing import List, Dict, Any, Tuple, Optional

bp = Blueprint("routes", __name__)


def deletar_usuario_logico(usuario: User) -> None:
    usuario.is_active = False
    db.session.commit()

@bp.route('/usuarios', methods=['GET'])
def get_todos_usuarios() -> Tuple[Response, int]:
    usuarios: List[User] = User.query.filter_by(is_active=True).all()
    return jsonify([usuario.to_dict() for usuario in usuarios]), 200

@bp.route('/usuarios', methods=['POST'])
def criar_usuario() -> Tuple[Response, int]:
    data: Dict[str, str] = request.json
    usuario = User(name=data['name'], email=data['email'], password=data['password'])
    db.session.add(usuario)
    db.session.commit()
    return jsonify(usuario.to_dict()), 201

@bp.route('/usuarios/<int:id>/admin', methods=['GET'])
def get_usuario_admin(id: int) -> Tuple[Response, int]:
    usuario: User = User.query.get_or_404(id)
    return jsonify(usuario.to_dict()), 200

@bp.route('/usuarios/<int:id>', methods=['GET'])
def get_usuario(id: int) -> Tuple[Response, int]:
    usuario: Optional[User] = User.query.get(id)

    if usuario.is_active == False or not usuario:
        return jsonify({'error': 'Usuário não encontrado'}), 404
    
    return jsonify(usuario.to_dict()), 200

@bp.route('/usuarios/<int:id>', methods=['PUT'])
def atualizar_usuario(id: int) -> Tuple[Response, int]:
    usuario: User = User.query.get_or_404(id)

    try:
        data: Dict[str, Optional[str]] = request.json
        usuario.name = data.get('name', usuario.name)
        usuario.email = data.get('email', usuario.email)
        usuario.password = data.get('password', usuario.password)
        db.session.commit()
        return jsonify(usuario.to_dict()), 200
    except KeyError as ke:
        return jsonify({'error': f"Campo obrigatório ausente: {str(ke)}"}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Erro ao atualizar o usuário.', 'detalhes': str(e)}), 500

@bp.route('/usuarios/<int:id>', methods=['DELETE'])
def deletar_usuario(id: int) -> Tuple[Response, int]:
    usuario: Optional[User] = User.query.get(id)

    if not usuario:
        return jsonify({'error': 'Usuário não encontrado'}), 404
    
    try:
        deletar_usuario_logico(usuario)
        return jsonify({'message': 'Usuário deletado com sucesso'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
