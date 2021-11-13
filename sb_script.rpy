init:
    $ mods["sb_start_play"]=u"Собачьи будни"

init: 
    image sb_behindd = "mods/dog/images/behind.jpg"
    image sb_black = "#000000" 
    image sb_xxx = "mods/dog/images/dogxxx.jpg" 
    image sb_red = "#ff2400"
    image sb_running: 
        'mods/dog/images/running1.png' with dspr
        pause(0.2) 
        'mods/dog/images/running2.png' with dspr
        pause(0.2) 
        'mods/dog/images/running3.png' with dspr
        pause(0.2)
        repeat 
    image sb_youdied = "mods/dog/images/youdied.png" 

init: 
    image un sad body far = im.MatrixColor( im.Composite((675,1080), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) )
    
init:
    $ begom = "mods/dog/music/begom domoy nahyi.mp3" 
    $ doglove = "mods/dog/music/doglove.mp3" 
    $ podval = "mods/dog/music/podval.mp3"
    $ guru = "mods/dog/music/guru.mp3" 
    $ speed = "mods/dog/music/speed.mp3"
    
init: 
    $ drinkwater = "mods/dog/sounds/drinkwater.mp3" 
    $ evilmeow = "mods/dog/sounds/evilmeow.mp3"
    $ gav = "mods/dog/sounds/gav.mp3" 
    $ laughing = "mods/dog/sounds/laughing.mp3" 
    $ lick = "mods/dog/sounds/lick.mp3" 
    $ meat = "mods/dog/sounds/meat.mp3"
    $ moan = "mods/dog/sounds/moan.mp3" 
    $ noeyes = "mods/dog/sounds/noeyes.mp3"
    $ pain = "mods/dog/sounds/pain.mp3"
    $ piss = "mods/dog/sounds/piss.mp3" 
    $ sled = "mods/dog/sounds/sled.mp3"
    $ sniffing = "mods/dog/sounds/sniffing.mp3" 
    
init: 
    transform sb_begg:
        zoom 1.05 anchor (48, 27)
        ease 0.10 pos (0,0)
        ease 0.10 pos (25, 25)
        ease 0.10 pos (0, 0)
        ease 0.10 pos (-25, 25)
        repeat 
    
    transform sb_shag:
        zoom 1.10 anchor (48, 27)
        ease 0.30 pos (0,0)
        ease 0.30 pos (25, 25)
        ease 0.30 pos (0, 0)
        ease 0.30 pos (-25, 25)
        repeat 
    
    transform sb_nightfilter:
        matrixcolor SaturationMatrix(0.8) * BrightnessMatrix(-0.1) * TintMatrix((115, 115, 165)) 

    transform blvrred: 
        mesh True 
        shader "sb.blurred" 
        u_resolution (1920, 1080) 
        u_mouse (960, 540)

init python: 
    renpy.register_shader("sb.blurred", variables=""" 
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform vec2 u_resolution; 
        uniform vec2 u_mouse;
    """, vertex_300="""
        v_tex_coord = a_tex_coord;
    """, fragment_300=""" 

        const int nsamples = 10;
        vec2 center = u_mouse.xy /u_resolution.xy;
	    float blurStart = 1.0;
        float blurWidth = 0.1;

    
	    vec2 uv = v_tex_coord;
    
        uv -= center;
        float precompute = blurWidth * (1.0 / float(nsamples - 1));
    
        vec4 color = vec4(0.0);
        for(int i = 0; i < nsamples; i++)
        {
            float scale = blurStart + (float(i)* precompute);
            color += texture2D(tex0, uv * scale + center);
        }
    
    
        color /= float(nsamples);
    
	    gl_FragColor = color;                              

    """) 
    
    
    
label sb_start_play:
    window hide 
    stop music fadeout 1
    stop sound fadeout 1                                                                                                                  
    stop sound2 fadeout 1
    stop sound3 fadeout 1
    stop sound_loop fadeout 1
    stop sound_loop2 fadeout 1
    stop sound_loop3 fadeout 1
    stop voice fadeout 1
    stop ambience fadeout 1
    scene sb_black with fade
    $ renpy.pause (2.0) 
    $ day_time()
    window show
    "Эпиграф нахуй." 
    "Бегают два пса по двору, один старый, а другой молодой. Наткнулись на кучу отбросов. Старый командует - жрать!" 
    "Поели, бегут дальше, видят суку. Старый командует - ебать!" 
    "Сделали дело, бегут дальше, видят - Икарус горит, ну они забежали в него и сгорели." 
    window hide 
    $ renpy.pause(1.0) 
    scene bg int_bus with fade: 
        anchor(0,0)
        block: 
            linear 0.1 pos (0,2)
            linear 0.1 pos (0,0)
            linear 0.1 pos (2,0)
            linear 0.1 pos (0,0) 
            repeat
    play music music_list["no_tresspassing"]
    play ambience sfx_bus_idle
    $ persistent.sprite_time = 'day' 
    $ renpy.pause (2.0) 
    $ _window_show(dissolve) 
    "Что, опять в Хуенок, что ли?" 
    "А, ну ладно. Как меня уже все это заебало, вы бы знали." 
    "Каждый ебучий раз одно и то же." 
    "Хоть бы раз что-то новое было." 
    "..." 
    stop ambience 
    play sound sfx_bus_stop 
    scene bg int_bus with vpunch
    th "О, моя остановочка."  
    window hide 
    play sound sfx_ikarus_open_doors 
    $ renpy.pause(2.5)
    scene bg ext_bus with fade 
    play sound sfx_intro_bus_transition 
    "Я вывалился из автобуса, дабы не упреть, оперся об одну из статуй на входе, тихонько перданул и начал ждать, когда же косичка высунется из-за ворот." 
    window hide
    $ renpy.pause (2.0) 
    scene bg ext_camp_entrance_day
    with dissolve2 
    $ renpy.pause (1.0)
    show sl normal pioneer far at center with dissolve
    window show 
    "Ну и вот через пару минут из-за ворот показались сначала косички, а потом и сама их хозяйка." 
    show sl smile pioneer at center with dspr
    "Увидела меня и начала подходить и улыбаться так неприятно." 
    sl "Привет, ты, наверное, только что приехал?" 
    th "А как ты догадалась-то?"
    me "Пьиветь, ти нявеняе тёко сьто пиехаль?" 
    show sl scared pioneer at center with dspr
    "Челюсть этой тупой пизды моментально отвисла ниже ее кос.{w} Причем верхняя челюсть." 
    "Мне даже на мгновение стало стыдно, что я ее обидел." 
    "..." 
    show sl angry pioneer at center with dspr 
    sl "Ты меня слышишь вообще?" 
    me "Ти меня слиси... Ой, то есть, что, прости?" 
    show sl sad pioneer at center with dspr 
    sl "Я говорю - найдешь вожатую и сам у нее все спросишь. Мне некогда, у меня дела." 
    hide sl with dissolve 
    th "Ну ок. А если бы я тут в самом деле в первый раз был, то что тогда?" 
    th "Хотя, это уже интересненько. Если с самого начала пошла такая музыка, то может, мне и отдельный домик найдут?" 
    "Ладно, пойду я...{w=1} {i}искать{/i} вожатую." 
    window hide 
    $ renpy.pause (2.0) 
    scene bg ext_house_of_mt_day
    with dissolve
    window show
    play ambience ambience_camp_center_day fadein 5 
    $ renpy.pause (2.0) 
    "В очередной раз понаблюдав за тем, как Ульяна применяла к Лене скафизм на минималках, и едва не огребя от Алисы пиздов, я добрел до дома ОД." 
    th "Мам, открывай, это я, твой блудный сынок." 
    hide window 
    play sound sfx_knock_door2 
    stop music fadeout 1.5 
    $ renpy.pause (1.5) 
    play sound sfx_open_dooor_campus_1 
    $ renpy.pause (0.5) 
    scene bg int_house_of_mt_day 
    with fade 
    stop ambience
    play music music_list["smooth_machine"]
    $ renpy.pause (1.0) 
    show mt normal pioneer far at center with dissolve
    window show 
    "Я вошел и увидел сахарную царицу всея Совенка." 
    th "Ничуть не изменилась.{w=1} Да и с чего бы..." 
    "..."
    "Ну что, когда уже наконец-то что-нибудь произойдет?.." 
    mtp "Пришёл-таки!{w} Отлично!{w} Меня Ольга Дмитриевна зовут, я вожатая."
    th "А я думал, насрано." 
    show mt normal pioneer at center with dissolve
    "Она подошла ближе." 
    th "Не подходи, зашибу."
    mt "Мы тебя с утра ждём." 
    "..." 
    th "{i}Твои родители мне звонили, телефона нет, автобус не приедет{/i}, блаблабла..." 
    th "{i}Вот твоя новая форма, не забудь про обед,{/i}{w=0.5}{nw}" 
    $ night_time()
    $ persistent.sprite_time = "night" 
    scene bg int_house_of_mt_night 
    show mt normal pioneer at center 
    with fade 
    extend " {i}домиков пустых нет, спать будешь здесь...{/i}"
    "Блядь, опять что ли пустых домиков нет? А нахуя тогда я надеялся, что хоть в этот раз будут?.." 
    "Сука, сколько можно-то уже?" 
    "И еще - когда мелкую пизду подвесят вниз башкой на входе в столовую?" 
    window hide 
    $ renpy.pause (0.5) 
    scene cg d2_mt_undressed with fade 
    $ persistent.sprite_time = "day" 
    $ day_time()
    $ renpy.pause (0.5) 
    show cg d2_mt_undressed_2 with dspr
    window show 
    th "{i}Как тебе блджад не стыдно, стучаться надо, кыш отсюда{/i}..." 
    th "Чего я там не видел-то, чтоб стыдиться..." 
    window hide
    $ renpy.pause (1.5) 
    play ambience ambience_camp_center_day fadein 3
    scene bg ext_house_of_mt_day 
    show mt normal panama pioneer at center
    with fade 
    stop music fadeout 1.5 
    $ renpy.pause (1.5) 
    window show
    mt "Так, куда же мне тебя поселить?" 
    me "А, может..." 
    "Но она не дала мне договорить, брякнув такое, что мне даже сначала показалось, что я ослышался."
    show mt sad panama pioneer at right with dspr
    mt "Прости, Семен, все домики заняты. Вчера просто некогда было решать этот вопрос." 
    mt "Не с собой же мне тебя селить." 
    mt "Поживи-ка ты пока что...{w=1.5} в собачьей конуре." 
    play sound sfx_scary_sting 
    me "{size=50}{cps=20}ЧЕГО, БЛЯДЬ?{/cps}{/size}" with vpunch 
    show mt surprise panama pioneer at right with dspr 
    mt "Ну чего неясного, будешь жить в собачьей конуре. И что это еще за выражения при мне?" 
    mt "Саша, Сережа, покажите Семену, где он будет жить." 
    show el normal pioneer at left 
    show sh normal pioneer at center 
    with moveinleft
    el "..." 
    sh "..." 
    "Местные образованные кадры мигом нарисовались передо мной{w=1}{nw}" 
    show el normal pioneer close at left 
    show sh normal pioneer close at center 
    with Dissolve(0.5) 
    play music begom 
    extend " и начали приближаться с намерением препроводить меня в мой {i}домик{/i} силой." 
    "Я подпустил блондина к себе поближе,{w=1}{nw}" 
    play sound sfx_punch_washstand
    hide el with easeoutbottom 
    extend " боднул его лбом прям промеж глаз и{w=1}{nw}" with vpunch
    show sh scared pioneer close at center 
    extend " дал драпа." 
    me "Руки прочь от советской власти!!!"
    play ambience sfx_run_forest
    hide sh 
    hide mt 
    with dspr 
    mt "Ну что вы как пеньки тупые, догоняйте его, быстро!!! Виоле скажите, пусть {i}усыпит{/i} его при необходимости!!!" 
    window hide 
    $ renpy.pause (1.5, hard=True) 
    scene bg ext_houses_day at sb_begg 
    show el fingal pioneer close at center zorder 2: 
        xpos 0.35 zoom 1.0 ypos 0.16
        ease 0.1 xpos 0.35634 ypos 0.1732
        ease 0.1 xpos 0.34 ypos 0.1632
        ease 0.1 xpos 0.3456 ypos 0.193
        ease 0.1 xpos 0.36353 ypos 0.1724
        ease 0.1 xpos 0.35 ypos 0.16
        repeat
    show sh rage pioneer close at center zorder 3: 
        xpos 0.5 zoom 1.0 ypos 0.2
        ease 0.1 xpos 0.49 ypos 0.12
        ease 0.1 xpos 0.51 ypos 0.24
        ease 0.1 xpos 0.505 ypos 0.21
        ease 0.1 xpos 0.495 ypos 0.16
        ease 0.1 xpos 0.5 ypos 0.2
        repeat
    show sb_running zorder 4 
    with fade 
    $ renpy.pause (4.5, hard=True)
    scene bg ext_library_day at sb_begg  
    show el fingal pioneer close at center zorder 2: 
        xpos 0.35 zoom 1.0 ypos 0.16
        ease 0.1 xpos 0.35634 ypos 0.1732
        ease 0.1 xpos 0.34 ypos 0.1632
        ease 0.1 xpos 0.3456 ypos 0.193
        ease 0.1 xpos 0.36353 ypos 0.1724
        ease 0.1 xpos 0.35 ypos 0.16
        repeat
    show sh rage pioneer close at center zorder 3: 
        xpos 0.5 zoom 1.0 ypos 0.2
        ease 0.1 xpos 0.49 ypos 0.12
        ease 0.1 xpos 0.51 ypos 0.24
        ease 0.1 xpos 0.505 ypos 0.21
        ease 0.1 xpos 0.495 ypos 0.16
        ease 0.1 xpos 0.5 ypos 0.2
        repeat    
    show sb_running zorder 4 
    with wipeleft 
    $ renpy.pause (4.5, hard=True) 
    scene bg ext_aidpost_day at sb_begg  
    show el fingal pioneer close at center zorder 2: 
        xpos 0.35 zoom 1.0 ypos 0.16
        ease 0.1 xpos 0.35634 ypos 0.1732
        ease 0.1 xpos 0.34 ypos 0.1632
        ease 0.1 xpos 0.3456 ypos 0.193
        ease 0.1 xpos 0.36353 ypos 0.1724
        ease 0.1 xpos 0.35 ypos 0.16
        repeat
    show sh rage pioneer close at center zorder 3: 
        xpos 0.5 zoom 1.0 ypos 0.2
        ease 0.1 xpos 0.49 ypos 0.12
        ease 0.1 xpos 0.51 ypos 0.24
        ease 0.1 xpos 0.505 ypos 0.21
        ease 0.1 xpos 0.495 ypos 0.16
        ease 0.1 xpos 0.5 ypos 0.2
        repeat
    show sb_running zorder 4 
    with wipeleft 
    $ renpy.pause (4.5, hard=True) 
    scene bg ext_musclub_day at sb_begg  
    show el fingal pioneer close at center zorder 2: 
        xpos 0.35 zoom 1.0 ypos 0.16
        ease 0.1 xpos 0.35634 ypos 0.1732
        ease 0.1 xpos 0.34 ypos 0.1632
        ease 0.1 xpos 0.3456 ypos 0.193
        ease 0.1 xpos 0.36353 ypos 0.1724
        ease 0.1 xpos 0.35 ypos 0.16
        repeat
    show sh rage pioneer close at center zorder 3: 
        xpos 0.5 zoom 1.0 ypos 0.2
        ease 0.1 xpos 0.49 ypos 0.12
        ease 0.1 xpos 0.51 ypos 0.24
        ease 0.1 xpos 0.505 ypos 0.21
        ease 0.1 xpos 0.495 ypos 0.16
        ease 0.1 xpos 0.5 ypos 0.2
        repeat
    show cs shy stethoscope close at center zorder 4: 
        xpos 0.65 zoom 1.0 ypos 0.21
        ease 0.1 xpos 0.64 ypos 0.22
        ease 0.1 xpos 0.66 ypos 0.20
        ease 0.1 xpos 0.645 ypos 0.2023
        ease 0.1 xpos 0.6534 ypos 0.216
        ease 0.1 xpos 0.65 ypos 0.21
        repeat
    show sb_running zorder 5 
    with wipeleft 
    $ renpy.pause (4.5, hard=True) 
    scene bg ext_dining_hall_away_day at sb_begg  
    show el fingal pioneer close at center zorder 2: 
        xpos 0.35 zoom 1.0 ypos 0.16
        ease 0.1 xpos 0.35634 ypos 0.1732
        ease 0.1 xpos 0.34 ypos 0.1632
        ease 0.1 xpos 0.3456 ypos 0.193
        ease 0.1 xpos 0.36353 ypos 0.1724
        ease 0.1 xpos 0.35 ypos 0.16
        repeat
    show sh rage pioneer close at center zorder 3: 
        xpos 0.5 zoom 1.0 ypos 0.2
        ease 0.1 xpos 0.49 ypos 0.12
        ease 0.1 xpos 0.51 ypos 0.24
        ease 0.1 xpos 0.505 ypos 0.21
        ease 0.1 xpos 0.495 ypos 0.16
        ease 0.1 xpos 0.5 ypos 0.2
        repeat
    show cs shy stethoscope close at center zorder 4: 
        xpos 0.65 zoom 1.0 ypos 0.21
        ease 0.1 xpos 0.64 ypos 0.22
        ease 0.1 xpos 0.66 ypos 0.20
        ease 0.1 xpos 0.645 ypos 0.2023
        ease 0.1 xpos 0.6534 ypos 0.216
        ease 0.1 xpos 0.65 ypos 0.21
        repeat
    show sb_running zorder 5 
    with wipeleft 
    $ renpy.pause (4.5, hard=True)
    scene bg ext_path2_day at sb_begg  
    show el fingal pioneer close at center zorder 2: 
        xpos 0.35 zoom 1.0 ypos 0.16
        ease 0.1 xpos 0.35634 ypos 0.1732
        ease 0.1 xpos 0.34 ypos 0.1632
        ease 0.1 xpos 0.3456 ypos 0.193
        ease 0.1 xpos 0.36353 ypos 0.1724
        ease 0.1 xpos 0.35 ypos 0.16
        repeat
    show sh rage pioneer close at center zorder 3: 
        xpos 0.5 zoom 1.0 ypos 0.2
        ease 0.1 xpos 0.49 ypos 0.12
        ease 0.1 xpos 0.51 ypos 0.24
        ease 0.1 xpos 0.505 ypos 0.21
        ease 0.1 xpos 0.495 ypos 0.16
        ease 0.1 xpos 0.5 ypos 0.2
        repeat
    show cs shy stethoscope close at center zorder 4: 
        xpos 0.65 zoom 1.0 ypos 0.21
        ease 0.1 xpos 0.64 ypos 0.22
        ease 0.1 xpos 0.66 ypos 0.20
        ease 0.1 xpos 0.645 ypos 0.2023
        ease 0.1 xpos 0.6534 ypos 0.216
        ease 0.1 xpos 0.65 ypos 0.21
        repeat
    show sb_running zorder 5 
    with wipeleft 
    $ renpy.pause (4.5, hard=True) 
    scene bg ext_playground_day at sb_begg  
    show el fingal pioneer close at center zorder 2: 
        xpos 0.35 zoom 1.0 ypos 0.16
        ease 0.1 xpos 0.35634 ypos 0.1732
        ease 0.1 xpos 0.34 ypos 0.1632
        ease 0.1 xpos 0.3456 ypos 0.193
        ease 0.1 xpos 0.36353 ypos 0.1724
        ease 0.1 xpos 0.35 ypos 0.16
        repeat
    show sh rage pioneer close at center zorder 3: 
        xpos 0.5 zoom 1.0 ypos 0.2
        ease 0.1 xpos 0.49 ypos 0.12
        ease 0.1 xpos 0.51 ypos 0.24
        ease 0.1 xpos 0.505 ypos 0.21
        ease 0.1 xpos 0.495 ypos 0.16
        ease 0.1 xpos 0.5 ypos 0.2
        repeat
    show cs shy stethoscope close at center zorder 4: 
        xpos 0.65 zoom 1.0 ypos 0.21
        ease 0.1 xpos 0.64 ypos 0.22
        ease 0.1 xpos 0.66 ypos 0.20
        ease 0.1 xpos 0.645 ypos 0.2023
        ease 0.1 xpos 0.6534 ypos 0.216
        ease 0.1 xpos 0.65 ypos 0.21
        repeat
    show sb_running zorder 5 
    with wipeleft 
    $ renpy.pause (4.5, hard=True) 
    scene bg black with wipeleft 
    $ renpy.pause (1.0, hard=True) 
    show text ("Прошло несколько часов") zorder 1 at truecenter with dissolve 
    $ renpy.pause (2.0, hard=True) 
    hide text with dissolve 
    $ persistent.sprite_time = 'night' 
    $ night_time()
    $ renpy.pause (1.0, hard=True) 
    scene bg ext_library_night at sb_begg  
    show el fingal pioneer close at center zorder 2: 
        xpos 0.35 zoom 1.0 ypos 0.16
        ease 0.1 xpos 0.35634 ypos 0.1732
        ease 0.1 xpos 0.34 ypos 0.1632
        ease 0.1 xpos 0.3456 ypos 0.193
        ease 0.1 xpos 0.36353 ypos 0.1724
        ease 0.1 xpos 0.35 ypos 0.16
        repeat
    show sh rage pioneer close at center zorder 3: 
        xpos 0.5 zoom 1.0 ypos 0.2
        ease 0.1 xpos 0.49 ypos 0.12
        ease 0.1 xpos 0.51 ypos 0.24
        ease 0.1 xpos 0.505 ypos 0.21
        ease 0.1 xpos 0.495 ypos 0.16
        ease 0.1 xpos 0.5 ypos 0.2
        repeat
    show cs normal stethoscope close at center zorder 4: 
        xpos 0.65 zoom 1.0 ypos 0.21
        ease 0.1 xpos 0.64 ypos 0.22
        ease 0.1 xpos 0.66 ypos 0.20
        ease 0.1 xpos 0.645 ypos 0.2023
        ease 0.1 xpos 0.6534 ypos 0.216
        ease 0.1 xpos 0.65 ypos 0.21
        repeat 
    show sb_running zorder 5
    with fade 
    $ renpy.pause (4.5, hard=True)
    scene bg ext_aidpost_night at sb_begg  
    show el fingal pioneer close at center zorder 2: 
        xpos 0.35 zoom 1.0 ypos 0.16
        ease 0.1 xpos 0.35634 ypos 0.1732
        ease 0.1 xpos 0.34 ypos 0.1632
        ease 0.1 xpos 0.3456 ypos 0.193
        ease 0.1 xpos 0.36353 ypos 0.1724
        ease 0.1 xpos 0.35 ypos 0.16
        repeat
    show sh rage pioneer close at center zorder 3: 
        xpos 0.5 zoom 1.0 ypos 0.2
        ease 0.1 xpos 0.49 ypos 0.12
        ease 0.1 xpos 0.51 ypos 0.24
        ease 0.1 xpos 0.505 ypos 0.21
        ease 0.1 xpos 0.495 ypos 0.16
        ease 0.1 xpos 0.5 ypos 0.2
        repeat
    show cs normal stethoscope close at center zorder 4: 
        xpos 0.65 zoom 1.0 ypos 0.21
        ease 0.1 xpos 0.64 ypos 0.22
        ease 0.1 xpos 0.66 ypos 0.20
        ease 0.1 xpos 0.645 ypos 0.2023
        ease 0.1 xpos 0.6534 ypos 0.216
        ease 0.1 xpos 0.65 ypos 0.21
        repeat 
    show sb_running zorder 5
    with wipeleft 
    $ renpy.pause (4.5, hard=True) 
    scene bg ext_dining_hall_away_night at sb_begg  
    show el fingal pioneer close at center zorder 2: 
        xpos 0.35 zoom 1.0 ypos 0.16
        ease 0.1 xpos 0.35634 ypos 0.1732
        ease 0.1 xpos 0.34 ypos 0.1632
        ease 0.1 xpos 0.3456 ypos 0.193
        ease 0.1 xpos 0.36353 ypos 0.1724
        ease 0.1 xpos 0.35 ypos 0.16
        repeat
    show sh rage pioneer close at center zorder 3: 
        xpos 0.5 zoom 1.0 ypos 0.2
        ease 0.1 xpos 0.49 ypos 0.12
        ease 0.1 xpos 0.51 ypos 0.24
        ease 0.1 xpos 0.505 ypos 0.21
        ease 0.1 xpos 0.495 ypos 0.16
        ease 0.1 xpos 0.5 ypos 0.2
        repeat
    show cs normal stethoscope close at center zorder 4: 
        xpos 0.65 zoom 1.0 ypos 0.21
        ease 0.1 xpos 0.64 ypos 0.22
        ease 0.1 xpos 0.66 ypos 0.20
        ease 0.1 xpos 0.645 ypos 0.2023
        ease 0.1 xpos 0.6534 ypos 0.216
        ease 0.1 xpos 0.65 ypos 0.21
        repeat 
    show sb_running zorder 5
    with wipeleft 
    $ renpy.pause (4.5, hard=True) 
    scene bg ext_house_of_mt_night at sb_begg  
    show el fingal pioneer close at center zorder 2: 
        xpos 0.35 zoom 1.0 ypos 0.16
        ease 0.1 xpos 0.35634 ypos 0.1732
        ease 0.1 xpos 0.34 ypos 0.1632
        ease 0.1 xpos 0.3456 ypos 0.193
        ease 0.1 xpos 0.36353 ypos 0.1724
        ease 0.1 xpos 0.35 ypos 0.16
        repeat
    show sh rage pioneer close at center zorder 3: 
        xpos 0.5 zoom 1.0 ypos 0.2
        ease 0.1 xpos 0.49 ypos 0.12
        ease 0.1 xpos 0.51 ypos 0.24
        ease 0.1 xpos 0.505 ypos 0.21
        ease 0.1 xpos 0.495 ypos 0.16
        ease 0.1 xpos 0.5 ypos 0.2
        repeat
    show cs normal stethoscope close at center zorder 4: 
        xpos 0.65 zoom 1.0 ypos 0.21
        ease 0.1 xpos 0.64 ypos 0.22
        ease 0.1 xpos 0.66 ypos 0.20
        ease 0.1 xpos 0.645 ypos 0.2023
        ease 0.1 xpos 0.6534 ypos 0.216
        ease 0.1 xpos 0.65 ypos 0.21
        repeat 
    show pi smile at center zorder 5: 
        xpos 0.85 zoom 1.3 ypos 0.21
        ease 0.1 xpos 0.84 ypos 0.22
        ease 0.1 xpos 0.86 ypos 0.20
        ease 0.1 xpos 0.845 ypos 0.2023
        ease 0.1 xpos 0.8534 ypos 0.216
        ease 0.1 xpos 0.85 ypos 0.21
        repeat 
    show sb_running zorder 5
    with wipeleft 
    $ renpy.pause (4.5, hard=True) 
    window show 
    pi "А ну стой, пидрила шерстяной{w=1.5}{nw}" 
    show blink zorder 6 
    stop ambience 
    stop music 
    play sound sfx_body_bump 
    "Какой-то левый хуйлан в пионерской форме сделал мне подножку, и я покатился по травке." 
    "Заебанная беготней Виола прикандыбала ко мне и вколола мне в правое полужопие какой-то транквилизатор, видимо." 
    "После чего приковыляли не менее заебанные два киберпидора, подняли меня и грубо поволокли в конуру." 
    "Я сам был заебан больше, чем они все вместе взятые, поэтому уже даже не сопротивлялся."
    window hide 
    $ renpy.pause (1.5) 
    scene bg ext_house_of_mt_night with fade 
    play ambience ambience_camp_center_day fadein 5 
    $ renpy.pause (1.5) 
    window show
    "Я скомкался в конуре, будучи не в силах двинуться, смотрел на домик ОД прямо напротив меня и кряхтел. У меня люто ломило спину." 
    "С каждым мгновением, проведенным в такой позе, у меня все больше и больше протекал чердак." 
    "Давление реальности было тяжело переносить." 
    "..." 
    th "Засунули меня, блядь, в собачью конуру, я че вам нахуй, пес что ли?" 
    th "...че я, пес что ли?" 
    th "...я пес..." 
    play music music_list["sparkles"]
    window hide 
    scene bg ext_house_of_mt_night at blvrred with Dissolve(12.5) 
    stop music 
    play sound moan 
    $ renpy.pause (7.5) 
    show layer master
    show blink 
    $ renpy.pause (3.5) 
    scene bg ext_house_of_mt_night with fade 
    $ renpy.pause (0.5) 
    window show 
    "Ррррр-гав." 
    "Разрешите представиться - Семен. Это кличка такая." 
    "Порода - пионерская борзая." 
    "..."
    th "Хорошо быть кисою, хорошо собакою." 
    th "Где хочу - пописию, где хочу - покакаю." 
    "Я засмотрелся на куст сирени, растущий рядом с огромной конурой." 
    th "Это же каких размеров псина должна в такой жить? Должно быть, какая-то очень большая сука." 
    "..." 
    "Ладно, похую." 
    "Мне просто очень захотелось писить." 
    "Я выполз из будки и сразу же почувствовал неудобство." 
    "Быстренько смекнув, в чем оно состояло, я начал когтями и зубами разрывать на себе тряпки, пока через 15 минут их на мне не осталось вообще." 
    "Стало гораздо удобнее. Я отряхнулся и, бодро засеменив к кусту сирени, задрал рядом с ним лапу." 
    window hide
    play sound piss 
    $ renpy.pause (6.5) 
    "Сделав свои дела, я поскреб в этом месте и разлегся около дверей огромной конуры." 
    show mt angry dress at center with dissolve
    mt "А ну кыш, место!!!" 
    hide mt with dissolve 
    "Я послушно засеменил обратно в свою будку." 
    window hide 
    show blink 
    $ renpy.pause (3.5) 
    show unblink 
    $ renpy.pause (1.5) 
    window show
    "Недолго полежав там, я вдруг понял, что мне просто до смертушки захотелось случки." 
    "Я выполз наружу и, навострив свой нюх, побежал по дорожке." 
    window hide
    stop ambience 
    play music doglove 
    scene bg ext_clubs_night at sb_begg with fade 
    $ renpy.pause (4.5, hard=True) 
    scene bg ext_dining_hall_away_night at sb_begg with wipeleft 
    $ renpy.pause (4.5, hard=True) 
    scene bg ext_library_night at sb_begg with wipeleft 
    $ renpy.pause (4.5, hard=True) 
    scene bg ext_playground_night at sb_begg with wipeleft 
    $ renpy.pause (1.5, hard=True) 
    show un normal sport at center with dissolve
    $ renpy.pause (1.5, hard=True) 
    show un grin sport at center with dspr 
    $ renpy.pause (1.5, hard=True) 
    show un laugh sport at center with dspr 
    $ renpy.pause (1.5, hard=True) 
    scene bg ext_path_night at sb_begg with wipeleft 
    $ renpy.pause (4.5, hard=True) 
    scene bg ext_path2_night at sb_begg with wipeleft 
    $ renpy.pause (4.5, hard=True) 
    scene bg ext_old_building_night_moonlight at sb_begg with wipeleft 
    $ renpy.pause (4.5, hard=True) 
    scene bg ext_stage_normal_night at sb_begg with wipeleft 
    $ renpy.pause (1.5, hard=True) 
    show dv normal pioneer2 at center with dissolve 
    $ renpy.pause (1.5, hard=True) 
    show dv grin pioneer2 at center with dspr 
    $ renpy.pause (1.5, hard=True) 
    show dv laugh pioneer2 at center with dspr 
    stop music fadeout 1.5
    $ renpy.pause (1.5, hard=True) 
    scene sb_behindd with fade 
    play ambience ambience_camp_center_day fadein 5 
    $ renpy.pause (1.5) 
    window show 
    "Ни одной суки и вообще никаких их следов я так и не нашел." 
    "Я очень устал от беготни, и мне хотелось жрать." 
    "Добежав до места, где пахло чем-то вкусненьким, я оказался у каких-то кустов, где, в самом деле, нашел предохрена рыбных потрохов и прочей вкуснятины." 
    "Вроде бы даже кого-то спугнул, но это не точно."
    "Нажравшись, я побежал обратно домой." 
    stop ambience
    scene sb_black with fade  
    play music music_list['lightness_radio_bus'] 
    $ day_time()
    "Все следующее утро и большую половину дня у меня просто пиздец как дико болел живот." 
    "Я обдристал весь порог возле огромной конуры, напротив которой жил, за что получил ногой прям по яйцам от огромной двуногой суки, жившей в ней." 
    "Оставшийся отрезок дня я даже боялся высунуться из своей будки, чтобы не получить еще раз. Да и живот не спешил проходить." 
    "С грустью в глазах я глядел на двери огромной конуры."
    "А еще никто за весь день ко мне не подошел и не попросил дать лапу." 
    window hide 
    $ renpy.pause (1.5) 
    scene bg ext_house_of_mt_night with fade 
    $ renpy.pause (1.5) 
    $ night_time()
    window show 
    "Темнело." 
    "Откуда-то неподалеку начала доноситься музыка и послышались какие-то оживленные голоса." 
    "К тому времени мне наконец-то полегчало." 
    "Захотелось пробежаться и освежиться. Потянуло к людям." 
    "Я вылез из будки, немного поискал у себя блох, не нашел, вылизал у себя под хвостом, поссал, поскреб, отряхнулся и побежал на шум." 
    window hide 
    $ renpy.pause (1.5)
    scene bg ext_square_night_party with fade 
    $ renpy.pause (1.5) 
    scene cg d3_disco with dspr
    window show 
    "На большой площадке столпилось много ребятни. Играла музыка, и все двигались." 
    me "({i}...щас спою...{/i})" 
    window hide 
    stop music fadeout 1.5 
    $ renpy.pause (1.5) 
    play sound moan 
    $ renpy.pause (4.5) 
    window show 
    "Музыка мигом прекратилась. Все уставились на меня и потом{w=1.5}{nw}" 
    play sound laughing 
    extend " почему-то загоготали." 
    show dv shocked pioneer far at left with dissolve 
    "Решив, что этот гогот означал, что моему появлению здесь рады, я подбежал прямо к толпе и обратил внимание на чьи-то ноги." 
    "Принюхавшись, я подполз к ногам, встал на задние лапы, высунул язык и начал ближнюю из этих самых ног самозабвенно трахать." 
    play sound laughing 
    "Раздался новый взрыв гогота..." 
    window hide 
    $ renpy.pause (3.5)
    show dv rage pioneer close at left with vpunch
    play sound sfx_lena_hits_alisa 
    $ renpy.pause (0.5) 
    play sound pain 
    window show 
    scene sb_black
    "И вот другой ногой я второй раз за день так получил по яйцам, что долго катался от боли по асфальту." 
    "..." 
    window hide 
    $ renpy.pause (4.5) 
    scene bg ext_square_night with fade 
    play ambience ambience_camp_center_day fadein 5 
    $ renpy.pause (1.5) 
    "Когда я очнулся, вокруг было уже совсем темно и пусто. Ну хотя бы боль от полученных сегодня пиздов утихла." 
    "Тоскливо тяфкнув, я принялся вылизывать под хвостом." 
    "Хотелось жрать и... просто хотелось жрать, еще о чем-то можно было забыть." 
    "Ярко светила луна. Надо бы обвыть ее. Ууу, луна ебаная."
    "Но не успев даже раскрыть пасть, я вдруг услышал, как кто-то позвал меня неподалеку." 
    un "Кууууть-куть-куть-куть." 
    "Я повернул голову." 
    show un grin pioneer far at center with dissolve 
    un "Семен, ко мне!" 
    th "Ага. Какая-то девочка."
    "Я поднялся на лапы и опасливо засеменил к ней." 
    show un grin pioneer close at center with dissolve 
    un "Хороший песик, умный." 
    "Девочка стала гладить меня по голове." 
    "Я довольно заурчал. Мне было приятно." 
    un "Рядом!!!" 
    hide un with easeoutright 
    "И тут она поманила меня за собой." 
    "Отправились мы, как я понял, в сторону леса." 
    play music podval 
    scene bg ext_path_night at sb_shag 
    with fade 
    "Подойдя к краю леса, девочка оглянулась. В тусклом свете ее глаза вспыхнули зеленоватым." 
    th "Странно. Я думал, у людей такого не бывает." 
    "Убедившись в чем-то своем, она пошла дальше в лес, по пути скидывая с себя шкуру." 
    th "Позерша ебаная."
    th "Хотя... вдруг ей тоже неудобно?" 
    th "Или что вообще? Что ей от меня нужно?" 
    scene bg ext_path2_night with fade 
    "Вдруг девочка остановилась и резко повернулась." 
    show un smile body at center with dissolve 
    "Странно. От нее пахло так же вкусно, как и от тех кустов, у которых я вчера наелся." 
    th "Даже вкуснее. Как будто рыба лежала на солнце несколько дней." 
    "Я уперся мордой в то ее место, из которого этот аромат исходил сильнее всего. Там было так мягко, влажно и... горячо?" 
    "Высунув язык, я прошелся по так вкусно пахнущей впадине и вновь издал довольное урчание." 
    "Девочка прижала руками мою голову, видимо, требуя, чтобы я продолжил, и легла на траву, тихо поскуливая." 
    window hide 
    $ renpy.pause (2.5) 
    stop ambience
    scene sb_xxx with fade 
    play ambience lick 
    $ renpy.pause (2.5) 
    un "О-оооооооххххххх..." 
    un "Ну же, Семка, давай вспоминай, кто ты..." 
    un "Ооооохххххххх... ну же, вспоминай... ооооооооййййййй, уфффффф..." 
    "А что я, блядь, вспоминать-то должен был?" 
    th "Запрятана там у нее кость или нет?" 
    th "Или что вообще?" 
    "Лизал я примерно полчаса. Вкус рыбы постепенно сошел на нет, при этом не чувствовалось вообще, что я что-то съел." 
    th "Какая-то неправильная рыба."
    "Я недовольно выпрямился." 
    window hide 
    $ renpy.pause (1.5) 
    stop ambience 
    scene bg ext_path2_night 
    show un surprise body close at center 
    with fade 
    $ renpy.pause (1.5) 
    window show
    "Девочка посмотрела куда-то под меня долгим таким взглядом, выражение которого я никак не мог расшифровать." 
    "..." 
    "Проследив за ее взглядом, я грустно заныл. Зачем она смотрела на мой хуй?" 
    th "Нет уж, каждому свое, тупая девка." 
    show un sad body close at center with dspr
    un "У тебя даже не..." 
    show un sad body far at center with dspr 
    un "ТЫ ТАК И НЕ ВСПОМНИЛ НИЧЕГО!!!" 
    hide un with easeoutbottom 
    "Она упала на землю и начала кататься по ней прям как я, когда мне ебнули по яйцам. Я боялся к ней приблизиться." 
    "Потом она доползла до одной из своих шкур, вытащила из нее что-то блеснувшее, провела себе по... лапе? Да, по лапе." 
    "С лапы стала стекать жидкость. Глаза девочки смотрели на меня в упор, но некоторое время спустя они погасли." 
    th "{b}Покатились глаза собачьи золотыми звездами...{/b}"
    "Блестящий предмет упал на землю, а тело распласталось по травке и больше не шевелилось." 
    th "Нихуя себе. А как она может так недвижимо лежать?" 
    window hide 
    $ renpy.pause (2.5) 
    scene cg d7_un_suicide at sb_nightfilter with fade: 
        pos (0,-360)
        linear 10.0 pos (0,0) 
    $ renpy.pause (10.0, hard=True) 
    window show 
    "Я подполз к ней и начал слизывать жидкость, все еще сочившуюся из ее лапы. Ммм, как же это было {i}вкусно{/i}." 
    th "Интересно, во всех людях есть такая?" 
    "Ни стона, ни звука, вообще никакого движения от нее так и не последовало." 
    "Кажется, она была мертва." 
    "Вообще поебать, уфф." 
    th "Значит, я мог ее сожрать." 
    play ambience meat
    "Я вгрызся в ее тело, захлебываясь хлынувшей в мою пасть жидкостью и чуть не поломав себе клыки." 
    th "Так вот где она прятала кости, а вовсе не там, где я сначала подумал." 
    "..." 
    "Съев немного мяса с ее боков и принявшись за симпатичные мясистые выступы, я вдруг услышал чьи-то шаги и на всякий случай вжался мордой в свою еду и затих." 
    sh "Да где ж этот бункер, едрить его в корень..." 
    "Дождавшись, пока голос и шаги не утихли вдалеке, я выпрямился. Наверное, надо было уже бежать домой." 
    th "Но куда девать мясцо?" 
    "..." 
    "Зарычав, я усиленно начал рыть под собой землю. Выкопав за довольно долгое время довольно хорошую яму, я столкнул остатки вкуснейшего мяса в нее и закопал." 
    stop ambience
    scene bg ext_path2_night with fade 
    "Ну вот. Пока мы шли сюда, я ничьих следов вроде не учуял. Так что думаю, теперь-то мою нычку никто не найдет." 
    "Отряхнувшись и вылизав под хвостом, я побежал в будку." 
    th "Хозяйка, я всю ночь тут спал, только не бейте меня."
    window hide 
    stop music fadeout 6.5 
    scene sb_black with Dissolve (6.5) 
    $ renpy.pause (2.5) 
    $ day_time()
    window show 
    "Сука, вот какого хуя всегда, когда я как следует наемся, мне на следующий день хреново?" 
    $ persistent.sprite_time = 'day' 
    "Я, отлежавшись и подождав, когда боль в животе утихнет, выполз из будки." 
    play ambience ambience_camp_center_day fadein 5
    scene bg ext_house_of_mt_day 
    show sl sad pioneer at left
    with fade 
    "У огромной конуры стояла девочка с пучком прутьев и сгребала им в совочек мое говно." 
    "Я на животе подполз к ней, но она замахнулась на меня." 
    sl "Кыш!!!" 
    "Потом она посмотрела на мою морду,{w=1.0}{nw}" 
    show sl scared pioneer at left 
    extend " сделала перепуганное выражение ебла,{w=1.0}{nw}" 
    play sound sfx_fall_grass 
    hide sl with easeoutleft 
    extend " и бросилась наутек."
    "Я вильнул хвостом и поплелся прочь." 
    scene bg ext_houses_day with fade 
    "Вдалеке у пункта кормежки слышались оживленные вопли."
    "Я был уже научен горьким опытом: если подойду к людям, то скорее всего, снова получу пизды." 
    "Но против моей воли меня все равно тянуло туда. Человек собаке друг, даже если пиздит ее иногда." 
    scene bg ext_dining_hall_near_day with fade 
    play music music_list['take_me_beautifully'] 
    "Подойдя туда, откуда я слышал голоса, я никого не нашел." 
    "Оно и понятно. Еще издали я увидел, как заметив меня, все начали разбегаться кто куда." 
    "Я тоскливо присел на крылечке и начал лакать воду из тазика." 
    "Я и сам слегка испугался морды, перепачканной чем-то бурым и пялившейся на меня из тазика..."
    window hide 
    play sound drinkwater 
    $ renpy.pause (3.5) 
    stop sound 
    window show
    show mt sad panama pioneer at left with moveinleft 
    show el scared pioneer at center with moveinleft 
    "Когда я напился, толпа уже потихоньку собралась рядом со мной." 
    el "Ольга Дмитриевна, я думаю, это бесполезно... Он его загрыз, я теперь более чем уверен." 
    show mt angry pioneer at left with dspr 
    mt "И что ты теперь хочешь сказать?" 
    el "Я? Н-ничего." 
    mt "Вот и пиздуй с глаз моих и пока не найдешь никаких признаков Шурика - даже не думай возвращаться!!!" 
    show mt sad panama pioneer at left with dspr
    mt "Не мог Семка никого сожрать. Он ла-ласковый и д-дружелюбный. Да, Семка?" 
    "Я поглядел на нее и{w=1.5}{nw}" 
    play sound gav 
    extend " гавкнул." 
    stop sound 
    hide mt with easeoutleft 
    "Двуногая сука перепуганно подскочила и съебалась. Сзади на ее юбке я заметил увеличивающееся коричневое пятно." 
    th "Эхехе, блядь." 
    "Я за ней не побежал. А стоило бы. Но я, чуя ее страх, ограничился лаем ей вдогонку." 
    window hide
    show blink 
    $ renpy.pause (2.0, hard=True)
    show text "Через час" at truecenter with dissolve 
    $ renpy.pause (2.0, hard=True) 
    hide text with dissolve 
    $ renpy.pause (2.0)
    scene bg ext_dining_hall_near_day
    show dv sad pioneer at left zorder 3
    show mt angry pioneer at center zorder 2
    show mi sad pioneer at center zorder 4: 
        xpos 0.65 
    show mz normal glasses pioneer at right zorder 1
    with fade 
    $ renpy.pause (1.0) 
    window show 
    mi "Ольга Дмитриевна, еще Лена куда-то пропала. А вдруг ее сожрали? Ну вдруг сожрали, а?.." 
    show mt rage pioneer at center zorder 5 with dspr 
    mt "Да заткнись ты нахуй со своей Леной, найдется она." 
    mt "У меня и так проблем выше крыши. Ты хоть понимаешь, что если мы не найдем Шурика, с меня исполком три шкуры сдерет?" 
    show mi sad pioneer at center zorder 6: 
        xpos 0.65
    mi "То есть с Шуриком... а с Леной, значит, нет..." 
    show mt angry pioneer at center zorder 7 with dspr
    dv "(...{i}{size=20}бля{/size}{/i}...)" 
    show mt rage pioneer at center zorder 8 with dspr
    mt "Дваче{w=0.2}{nw}" 
    show dv angry pioneer at left zorder 9 with dspr 
    extend "вская, ты куда это намылилась?" 
    dv "..." 
    mt "Не поняла. Если вы застали меня в неловком положении, меня теперь что, можно в хуй не ставить?" 
    window hide 
    hide dv with easeoutleft 
    $ renpy.pause (4.5, hard=True) 
    play sound sfx_muffled_explosion 
    show mt scared pioneer at center with vpunch 
    $ renpy.pause (3.5, hard=True) 
    window show 
    mt "..."
    mt "Ебанашка." 
    show el upset pioneer at left zorder 10 with easeinleft: 
        xpos 0.35
    el "Ольга Дмитриевна, вот все, что я нашел..." 
    show mt shocked pioneer at center zorder 11 with dspr
    mt "Ботинок?" 
    el "Да, ботинок." 
    mt "И где ты его нашел?" 
    el "В лесу, по дороге в старый лагерь." 
    show mt angry pioneer at center with dspr 
    mt "Дай-ка его сюда." 
    show mt angry pioneer close at center with dspr 
    "Взяв башмак из рук блондина, она сунула его мне под нос. Я недовольно заурчал. От башмака пахло отвратительно." 
    mt "След!!!" 
    "Мое тело напряглось. Я тут же рванулся, благо мерзкий запах от ботинка довольно отчетливо - даже слишком отчетливо - ощущался моим нюхом." 
    play sound sled
    scene bg ext_path2_day at sb_begg with fade 
    "Около едва заметной ямы у тропы след оборвался. Видимо, хозяин ботинка сиганул туда." 
    th "Мне что, прыгать туда самому?" 
    "..." 
    stop music 
    stop ambience
    play sound sfx_simon_fall_2 
    scene sb_black 
    "Собравшись с духом, я все-таки прыгнул." 
    window hide 
    $ renpy.pause (3.5) 
    scene bg int_catacombs_entrance with fade 
    play ambience ambience_catacombs_stones fadein 3 
    play music music_list['sunny_day'] 
    $ renpy.pause (1.5) 
    $ persistent.sprite_time = 'night' 
    $ night_time()
    window show
    "Чето как-то мне тут неуютно нихуя." 
    "Немного посидев на одном месте, я почесал лапой за ухом." 
    "Потом потянул носом. След все еще слабо, но ощущался." 
    "Это наполнило мое существование смыслом и заставило медленно поплестись дальше по темному коридору." 
    th "Я же пес или что? Думаю, в случае чего сориентировался бы. Ну там нечистая сила какая-нибудь нападет или где..." 
    window hide 
    $ renpy.pause (1.5) 
    scene bg int_catacombs_door with fade 
    $ renpy.pause (1.5) 
    window show 
    "..." 
    th "Открывай дверь, блядь, фас. Открывай дверь." 
    "Чем, лапами, что ли?" 
    th "Открывай. Открывай дверь! Сядь уже. Сидеть! Открывай!" 
    "Ррррр-гав!" 
    th "Чтобы открыто было!"
    "Как я ее буду лапами-то открывать?" 
    th "Открывай!" 
    "Покажи мне, как!" 
    th "Открывай!" 
    "Что {i}открывай{/i}, гав, как я буду лапами-то открывать? Че, совсем мудак что ли, покажи мне, как я буду открывать-то, епта!!!" 
    "Епта, блядь... как ими открывать, еб твою... Совсем ебанулись... бля, епта..." 
    th "Открывай, открывай, сука. Вот как, блядь, нужно открывать, вот, быстро. Быстро. Раз-раз! Открывай, открывай, открывай-открывай-открвй-открвй-откр-ывай! Открывай! Дверь! Открывай!"
    "Бля, у тебя получается классно, давай!" 
    th "Давай, работай!"
    "Пидорасы, блядь… Суки, блядь. Стальная дверь. Охуенно. Блядь. Сука, блядь. Не буду я в этом! Не буду я!"
    th "Пошёл нахуй тогда отсюда, пошёл, блядь, ничего не можешь сделать, пошел нахуй, говно!" 
    play sound sfx_open_metal_hatch
    stop ambience fadeout 2 
    "Короче, дверь каким-то совершенно невероятным хуем открылась. Шмагия какая-то."
    window hide 
    scene bg int_catacombs_living_nodoor
    with fade
    window show 
    "Я забежал в огромную пустую берлогу и начал присматриваться и принюхиваться."
    "Тут царил полнейший бардак. По всему чувствовалось, что тут не так давно побывало что-то здоровое, напуганное и, видимо, очкастое." 
    "Дверь в другой стене была выбита, и я, недолго думая, рванул туда, хлеща себя хвостом по бокам." 
    window hide
    play ambience ambience_catacombs fadein 3
    scene bg int_catacombs_hole with fade
    "По следу я добежал еще до одной дыры. Похоже, мне опять нужно пррр-ррыгать." 
    window hide 
    scene bg int_mine with fade 
    window show
    "Спрыгнув, я сразу же сделал неприятное открытие. След просто исчез и ну никак не чувствовался вообще."
    "Зато ощущался кое-какой другой запах." 
    "Тот самый запах, который меня ну очень разозлил." 
    "В этом подземелье пиздецки разило кошачьей ссаниной." 
    "Я яросто гавкнул и припал нюхом к земле, дабы вынюхать хотя бы кошку. Мне уже даже света было не нужно." 
    "Кошачий след становился все явственнее. Я не мог скрыть своего охотничьего азарта и время от времени заливисто лаял, от возбуждения впечатываясь башкой в стены." 
    th "А, может, и не от возбуждения вовсе, а от того что ну{cps=10}...{/cps}{w=1} все-таки немного света бы не помешало." 
    "..." 
    scene bg int_mine with fade 
    "За очередным поворотом я увидел большую неясную тень." 
    "Меня всего передернуло." 
    "В спертом воздухе подземелья запах кошачьего ссанья чувствовался все сильнее и сильнее." 
    "Связав одно с другим, я сделал вывод, что этой тенью и была ебучая кошка." 
    scene cg d4_uv_1 with fade
    "Забежав за поворот, я и в самом деле увидел здоровенную кошару, сидевшую на камне." 
    "Она нагло так на меня уставилась." 
    scene cg d4_uv with dspr
    dreamgirl "Ты кто нахуй?" 
    play sound gav 
    play music speed 
    "Разразившись лаем, я на нее набросился." 
    scene bg int_mine
    show uv shocked far at center 
    with flash 
    "Но немного не достал." 
    "Кошка вскочила с камня и убежала, а я припустил за ней, задрав хвост трубой и лая, как Цербер нахуй." 
    window hide
    scene bg int_mine at sb_begg 
    show uv surprise2 far at center zorder 1: 
        xpos 0.5 zoom 1.0 ypos 0.2
        ease 0.1 xpos 0.49 ypos 0.12
        ease 0.1 xpos 0.51 ypos 0.24
        ease 0.1 xpos 0.505 ypos 0.21
        ease 0.1 xpos 0.495 ypos 0.16
        ease 0.1 xpos 0.5 ypos 0.2
        repeat 
    show sb_running zorder 2
    with fade 
    $ renpy.pause (5.5, hard=True) 
    scene bg int_mine_crossroad at sb_begg 
    show uv surprise2 far at center zorder 1: 
        xpos 0.5 zoom 1.0 ypos 0.2
        ease 0.1 xpos 0.49 ypos 0.12
        ease 0.1 xpos 0.51 ypos 0.24
        ease 0.1 xpos 0.505 ypos 0.21
        ease 0.1 xpos 0.495 ypos 0.16
        ease 0.1 xpos 0.5 ypos 0.2
        repeat 
    show sb_running zorder 2 
    with wipeleft
    $ renpy.pause (5.5, hard=True) 
    scene bg int_mine_halt at sb_begg 
    show uv sad far at center zorder 1: 
        xpos 0.5 zoom 1.0 ypos 0.2
        ease 0.1 xpos 0.49 ypos 0.12
        ease 0.1 xpos 0.51 ypos 0.24
        ease 0.1 xpos 0.505 ypos 0.21
        ease 0.1 xpos 0.495 ypos 0.16
        ease 0.1 xpos 0.5 ypos 0.2
        repeat 
    show sb_running zorder 2
    with wipeleft 
    $ renpy.pause (5.5, hard=True) 
    scene bg int_mine_crossroad at sb_begg 
    show uv sad far at center zorder 1: 
        xpos 0.5 zoom 1.0 ypos 0.2
        ease 0.1 xpos 0.49 ypos 0.12
        ease 0.1 xpos 0.51 ypos 0.24
        ease 0.1 xpos 0.505 ypos 0.21
        ease 0.1 xpos 0.495 ypos 0.16
        ease 0.1 xpos 0.5 ypos 0.2
        repeat 
    show sb_running zorder 2
    with wipeleft
    $ renpy.pause (5.5, hard=True) 
    scene bg int_mine_halt at sb_begg 
    show uv upset at center zorder 1: 
        xpos 0.5 zoom 1.0 ypos 0.2
        ease 0.1 xpos 0.49 ypos 0.12
        ease 0.1 xpos 0.51 ypos 0.24
        ease 0.1 xpos 0.505 ypos 0.21
        ease 0.1 xpos 0.495 ypos 0.16
        ease 0.1 xpos 0.5 ypos 0.2
        repeat 
    show sb_running zorder 2
    with wipeleft 
    $ renpy.pause (5.5, hard=True) 
    scene bg int_mine_crossroad at sb_begg 
    show uv upset at center zorder 1: 
        xpos 0.5 zoom 1.0 ypos 0.2
        ease 0.1 xpos 0.49 ypos 0.12
        ease 0.1 xpos 0.51 ypos 0.24
        ease 0.1 xpos 0.505 ypos 0.21
        ease 0.1 xpos 0.495 ypos 0.16
        ease 0.1 xpos 0.5 ypos 0.2
        repeat 
    show sb_running zorder 2
    with wipeleft
    $ renpy.pause (5.5, hard=True) 
    scene bg int_mine_halt at sb_begg 
    show uv dontlike close at center zorder 1: 
        xpos 0.5 zoom 1.0 ypos 0.2
        ease 0.1 xpos 0.49 ypos 0.12
        ease 0.1 xpos 0.51 ypos 0.24
        ease 0.1 xpos 0.505 ypos 0.21
        ease 0.1 xpos 0.495 ypos 0.16
        ease 0.1 xpos 0.5 ypos 0.2
        repeat 
    show sb_running zorder 2
    with wipeleft 
    $ renpy.pause (5.5, hard=True) 
    scene bg int_mine_crossroad at sb_begg 
    show uv dontlike close at center zorder 1: 
        xpos 0.5 zoom 1.0 ypos 0.2
        ease 0.1 xpos 0.49 ypos 0.12
        ease 0.1 xpos 0.51 ypos 0.24
        ease 0.1 xpos 0.505 ypos 0.21
        ease 0.1 xpos 0.495 ypos 0.16
        ease 0.1 xpos 0.5 ypos 0.2
        repeat 
    show sb_running zorder 2
    with wipeleft
    $ renpy.pause (5.5, hard=True) 
    scene bg int_mine_door at sb_begg 
    show uv rage close at center zorder 1: 
        xpos 0.5 zoom 1.0 ypos 0.2
        ease 0.1 xpos 0.49 ypos 0.12
        ease 0.1 xpos 0.51 ypos 0.24
        ease 0.1 xpos 0.505 ypos 0.21
        ease 0.1 xpos 0.495 ypos 0.16
        ease 0.1 xpos 0.5 ypos 0.2
        repeat 
    show sb_running zorder 2
    with wipeleft 
    $ renpy.pause (5.5, hard=True) 
    scene bg int_mine_room_red 
    show uv rage close at center 
    with fade 
    $ renpy.pause (1.5, hard=True) 
    window show 
    "Наконец, я загнал кошку в угол и приготовился разодрать ее на куски." 
    "Но..." 
    window hide
    stop music 
    play sound evilmeow 
    $ renpy.pause (0.9) 
    play sound noeyes
    scene sb_red with Dissolve (0.6) 
    $ renpy.pause (1.0) 
    scene sb_black with Dissolve (1.0) 
    window show 
    "Что-то острое полоснуло мне по глазам." 
    "Я больше ничего не видел." 
    "Теплая и липкая жидкость стекала по моей морде." 
    th "Почему она так похожа по вкусу на тот кусок мяса..." 
    "Через мгновение пришла адская боль." 
    "{cps=15}Я не выдержал и заорал{/cps}{nw}" 
    window hide 
    play music guru noloop 
    $ renpy.pause (8.5) 
    window show 
    show pi smile at center with dissolve 
    pi "Аваххвхахавхвха ебануться..." 
    pi "Дааааа, ну такого пиздеца я не видывал ни разу..." 
    hide pi with dissolve
    window hide 
    $ renpy.pause (4.5) 
    scene sb_youdied with fade 
    $ renpy.pause (5.5)
    return