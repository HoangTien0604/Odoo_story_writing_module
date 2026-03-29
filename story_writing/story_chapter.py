# -*- coding: utf-8 -*-
from openerp.osv import fields, osv

class story_chapter(osv.osv):
    _name = 'story.chapter'
    _order = 'sequence asc'

    _columns = {
        'name': fields.char('Tiêu đề chương', size=200, required=True),
        'sequence': fields.integer('Thứ tự', required=True),
        'content': fields.text('Nội dung chương'),

        'story_id': fields.many2one(
            'story.story',
            'Thuộc truyện',
            required=True,
            ondelete='cascade'
        ),
    }

    _defaults = {
        'sequence': 1
    }

story_chapter()
