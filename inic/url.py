# coding: utf-8
fix = 'core.'
#common
ext = 'common.'
urls= (
    #admin
    r'/admin/',                         fix + 'room.Login',
    r'/admin/loges',                    fix + 'room.Loges',
    r'/admin/login',                    fix + 'room.Index',
    r'/admin/menu/([^\s/]+)/(\d*)/?(\d*)',    fix + 'room.Menu',
    r'/admin/tag',                      fix + 'room.Tag',
    r'/admin/advert/',                   fix + 'room.Advert',
    r'/admin/addlist',                  fix + 'room.Addlist',
    r'/admin/artlist',                  fix + 'room.Artlist',
    r'/admin/addart',                   fix + 'room.Addart',
    r'/admin/tain',                     fix + 'room.Tain',
    r'/admin/sys',                      fix + 'room.System',
    r'/admin/total',                    fix + 'room.Total',
    r'/admin/editor',                   fix + 'room.Editor',
    r'/admin/record/([^\s/]+)/?(\d*)',  fix + 'room.Record',
    r'/admin/deleter',                  fix + 'room.Deleter',
    #index
	r'/',                               fix + 'home.Index',
    r'/pay',                            fix + 'home.Cash',
	r'/info/(\d+)',                     fix + 'home.Info',
	r'/json.js',                        fix + 'home.Jsone',
    #other
	r'/upload/?',                       fix + 'others.Upload',
    r'/menmber/login',                  fix + 'menmber.Login',
    r'/menmber/center',                 fix + 'menmber.Index',
	#common
    '/(.*.ico)',                        ext + 'dispose.Static',
    r'/common/json',                    ext + 'dispose.Index',
)
