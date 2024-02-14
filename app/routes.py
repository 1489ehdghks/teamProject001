from flask import request, jsonify, render_template, redirect, url_for
from . import app, db
from app.models import TeamMember


@app.route('/')
def index():
    team_members = TeamMember.query.all() 
    return render_template('team.html', team_members=team_members)

@app.route('/create_team_member', methods=['GET', 'POST'])
def create_team_member():
    if request.method == 'POST':
        data = request.form
        new_member = TeamMember(
            username=data['username'],
            image_url=data['image_url'],
            mbti=data['mbti'],
            collabo_style=data['collabo_style'],
            advantage=data['advantage'],
            blog_url=data.get('blog_url')
        )
        db.session.add(new_member)
        db.session.commit()
        return redirect(url_for('index'))

    elif request.method == 'GET':
        return render_template('createMember.html')
    
@app.route('/delete_team_member/<int:member_id>', methods=['DELETE'])
def delete_team_member(member_id):
    member = TeamMember.query.get_or_404(member_id)
    db.session.delete(member)
    db.session.commit()
    return jsonify({'message': 'Team member deleted successfully'}), 200


@app.route('/edit_member/<int:member_id>')
def edit_member(member_id):
    member = TeamMember.query.get(member_id)
    if not member:
        return "Member not found", 404
    return render_template('editMember.html', member=member)

@app.route('/update_member/<int:member_id>', methods=['PUT'])
def update_member(member_id):
    data = request.json
    member = TeamMember.query.get(member_id)
    if not member:
        return jsonify({'message': 'Member not found'}), 404

    member.name = data.get('name')
    member.image_url = data.get('image_url')
    member.mbti = data.get('mbti')
    member.collabo_style = data.get('collabo_style')
    member.advantage = data.get('advantage')
    member.blog_url = data.get('blog_url')

    db.session.commit()
    return jsonify({'message': 'Member updated successfully'}), 200