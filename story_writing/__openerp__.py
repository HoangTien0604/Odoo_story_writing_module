{
    "name": "Viết Truyện",
    "version": "1.0",
    "author": "Đồng Hoàng Tiến",
    "description": "Module quản lý viết truyện bao gồm các chức năng như tạo truyện, chương cho tác giả, độc giả có thể xem các truyện đã công khai v.v.",
    "website": "",
    "category": "Writing",
    "depends": ["base"],
    "init_xml": [],
    "demo_xml": ["story_demo.xml"],
    "update_xml": [
        "security/story_security.xml",
        "security/story_rule.xml",
        "security/ir.model.access.csv",

        "story_view.xml",
        "story_chapter_view.xml",
        "story_menu.xml",

        "reader_view.xml"
    ],
    "active": False,
    "installable": True,
}
