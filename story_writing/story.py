# -*- coding: utf-8 -*-
from openerp.osv import fields, osv

class story(osv.osv):
    _name = 'story.story'

    _columns = {
        'name': fields.char('Tên truyện', size=100, required=True, translate=True),
        'writer': fields.char('Tác giả', size=100, required=True),
        'category': fields.selection([
            ('fantasy', 'Giả tưởng'),
            ('scifi', 'Khoa học viễn tưởng'),
            ('mystery', 'Bí ẩn'),
            ('romance', 'Lãng mạn'),
            ('horror', 'Kinh dị')
        ], 'Thể loại'),
        'published_date': fields.date('Ngày xuất bản'),
        'published': fields.boolean('Đã công bố?'),
        'synopsis': fields.text('Tóm tắt nội dung'),

        # 1–n
        'chapter_ids': fields.one2many(
            'story.chapter',
            'story_id',
            'Danh sách chương'
        ),
    }

    _defaults = {
        'published': False
    }

story()
