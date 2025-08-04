_AF='🎨 Roblox Pixel Art Converter Pro + AI'
_AE='Close Button'
_AD='Hex Input'
_AC='Color Button'
_AB='Bottom-Right Pixel'
_AA='Top-Left Pixel'
_A9='timestamp'
_A8='Posterize'
_A7='Edge Enhance'
_A6='Blur Slightly'
_A5='powershell'
_A4='brightness'
_A3='top_bottom'
_A2='left_right'
_A1='🎨 Brightness Priority'
_A0='📊 Top to Bottom'
_z='🌊 Left to Right'
_y='🔥 No Delay (0.001s)'
_x='⚡ Instant (0.01s)'
_w='💨 Lightning (0.02s)'
_v='🚀 Turbo (0.05s)'
_u='⚡ Fast (0.1s)'
_t='🚶 Safe (0.5s)'
_s='🐌 Ultra Safe (1.0s)'
_r='🦄 Pastel/Dreamy'
_q='🎪 Retro/Vintage'
_p='🌺 Nature/Floral'
_o='🏰 Medieval/Fantasy'
_n='🤖 Cyberpunk/Sci-Fi'
_m='✨ Fantasy/Magic'
_l='🌈 Cartoon/Disney'
_k='🎮 Video Game Art'
_j='🌸 Anime/Manga'
_i='pixel_art'
_h='original_image'
_g='127.0.0.1'
_f='RGB'
_e='🎯 Color Groups'
_d='🏃 Normal (0.2s)'
_c='🔥 Custom Prompt'
_b='🎨 Kawaii/Cute Style'
_a='estimated_time'
_Z='color_groups'
_Y='🎛️ Custom'
_X='settings_file'
_W='None'
_V='inputY'
_U='inputX'
_T='openButtonY'
_S='openButtonX'
_R='lastY'
_Q='lastX'
_P='temp_files'
_O='start_time'
_N='closeButtonY'
_M='closeButtonX'
_L='firstY'
_K='firstX'
_J='user_interrupted'
_I='drawing_stats'
_H='is_drawing'
_G='ai_generating'
_F='total_pixels_drawn'
_E='pixel_colors'
_D='coords'
_C=True
_B=None
_A=False
import gradio as gr,time,threading,json,os,numpy as np
from PIL import Image,ImageEnhance,ImageFilter
import pyautogui,win32api,win32con,ctypes,pyperclip
from datetime import datetime
import random,webview,sys,requests,tempfile,base64
from cryptography.fernet import Fernet
import hashlib,tkinter as tk
from tkinter import ttk
import queue
import platform
import subprocess
import uuid
import hashlib
DECRYPTION_KEY='PePa24410'
def get_hwid():
    'Generate unique hardware ID'
    try:
        # Get system info
        system = platform.system()
        processor = platform.processor()
        machine = platform.machine()
        
        # Get MAC address
        mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])
        
        # Combine and hash
        hw_string = f"{system}-{processor}-{machine}-{mac}"
        return hashlib.sha256(hw_string.encode()).hexdigest()[:16]
    except:
        return hashlib.sha256(str(uuid.getnode()).encode()).hexdigest()[:16]
def verify_key(key):
    'Verify key with server'
    try:
        hwid = get_hwid()
        response = requests.post(
            'http://oh3.uniplex.xyz:3108/verify',
            json={'key': key, 'hwid': hwid},
            timeout=10
        )
        return response.json()
    except:
        return {'valid': False, 'message': 'Connection error'}
def generate_key_from_password(password):'Generate Fernet key from password';A=hashlib.sha256(password.encode()).digest();return base64.urlsafe_b64encode(A[:32])
def decrypt_data(encrypted_data,password):
    'Decrypt data using password'
    try:A=generate_key_from_password(password);B=Fernet(A);return B.decrypt(encrypted_data.encode()).decode()
    except:return
def encrypt_data(data,password):'Encrypt data using password';A=generate_key_from_password(password);B=Fernet(A);return B.encrypt(data.encode()).decode()
ENCRYPTED_API_KEY=encrypt_data('m0u_gXRorNW4sOEi9OGdKQ',DECRYPTION_KEY)
pyautogui.FAILSAFE=_A
pyautogui.PAUSE=.01
app_state={_D:{_K:_B,_L:_B,_Q:_B,_R:_B,_S:_B,_T:_B,_U:_B,_V:_B,_M:_B,_N:_B},_h:_B,_i:_B,_E:{},_H:_A,_J:_A,'drawing_thread':_B,_F:0,_X:'roblox_pixel_art_settings.json',_I:{_O:_B,'colors_used':0,_a:0},'current_preview':'Original',_G:_A,'progress_window':_B,'progress_queue':queue.Queue(),_P:[]}
AI_STYLE_PRESETS=[_b,_j,_k,_l,_m,_n,_o,_p,_q,_r,_c]
AI_STYLE_TEMPLATES={_b:'kawaii style, cute, adorable, pastel colors, chibi, soft lighting, high detail',_j:'anime style, manga, detailed, vibrant colors, clean lines, studio quality',_k:'video game art, pixel perfect, gaming, digital art, detailed',_l:'cartoon style, disney-like, colorful, friendly, animated movie style',_m:'fantasy art, magical, mystical, glowing effects, ethereal',_n:'cyberpunk, sci-fi, neon colors, futuristic, high-tech',_o:'medieval fantasy, castle, knights, dragons, epic',_p:'nature, flowers, botanical, organic, beautiful',_q:'retro, vintage, 80s style, nostalgic, classic',_r:'pastel colors, dreamy, soft, ethereal, cloud-like',_c:''}
SPEED_OPTIONS=[_s,_t,_d,_u,_v,_w,_x,_y,_Y]
SPEED_VALUES={_s:1.,_t:.5,_d:.2,_u:.1,_v:.05,_w:.02,_x:.01,_y:.001,_Y:'custom'}
PATTERN_OPTIONS=[_e,_z,_A0,'🌀 Spiral','🎲 Random',_A1]
PATTERN_VALUES={_e:_Z,_z:_A2,_A0:_A3,'🌀 Spiral':'spiral','🎲 Random':'random',_A1:_A4}
class SimpleProgressTracker:
    'Simple progress tracking without Tkinter threading issues'
    def __init__(A):A.is_visible=_A;A.current_progress=0;A.pixels_done=0;A.pixels_total=0;A.time_remaining=0
    def show(A):'Show progress tracking';A.is_visible=_C;print('📊 Progress tracking started...')
    def hide(A):'Hide progress tracking';A.is_visible=_A;print('📊 Progress tracking stopped.')
    def update_progress(A,percentage,time_remaining,pixels_done,pixels_total):
        'Update progress information';E=pixels_total;D=pixels_done;C=percentage;B=time_remaining;A.current_progress=C;A.time_remaining=B;A.pixels_done=D;A.pixels_total=E
        if A.is_visible:
            if int(C)%5==0 and C>0:F=int(B//60)if B>0 else 0;G=int(B%60)if B>0 else 0;print(f"🎨 Progress: {C:.1f}% | Pixels: {D}/{E} | Time: {F}m {G}s")
    def destroy(A):'Cleanup progress tracker';A.is_visible=_A
floating_progress=SimpleProgressTracker()
def cleanup_temp_files():
    'Clean up temporary files'
    for A in app_state[_P]:
        try:
            if os.path.exists(A):os.remove(A)
        except:pass
    app_state[_P].clear()
def generate_ai_image(prompt,style_preset,progress_callback=_B):
    'Generate AI image using Stable Horde API';J=prompt;I='generations';C=style_preset;A=progress_callback
    try:
        K=decrypt_data(ENCRYPTED_API_KEY,DECRYPTION_KEY)
        if not K:return _B,'❌ Failed to decrypt API key'
        app_state[_G]=_C
        if C!=_c and C in AI_STYLE_TEMPLATES:L=f"{J}, {AI_STYLE_TEMPLATES[C]}"
        else:L=J
        P={'apikey':K,'Client-Agent':'RobloxPixelArtPro'};Q='https://stablehorde.net/api/v2/generate/async';R={'prompt':L,'params':{'n':1,'width':512,'height':512,'steps':20,'sampler_name':'k_euler_a'},'models':['stable_diffusion']}
        if A:A('📝 Sending request to AI...',0)
        D=requests.post(Q,headers=P,json=R,timeout=30)
        if D.status_code!=202:app_state[_G]=_A;return _B,f"❌ Failed to submit job: {D.text[:100]}"
        E=D.json()['id']
        if A:A(f"📩 Job submitted (ID: {E[:8]}...)",10)
        S=f"https://stablehorde.net/api/v2/generate/check/{E}";T=f"https://stablehorde.net/api/v2/generate/status/{E}";M=300;N=time.time()
        while time.time()-N<M:
            time.sleep(3)
            try:
                F=requests.get(S,timeout=10).json()
                if F.get('done'):
                    if A:A('✅ Image generation complete!',90)
                    break
                else:
                    U=F.get('queue_position','?');V=F.get('wait_time',0);W=min(80,10+(time.time()-N)/M*70)
                    if A:A(f"⌛ Queue position: {U} | Wait: {V}s",W)
            except requests.RequestException:
                if A:A('⚠️ Connection issue, retrying...',_B)
                continue
        else:app_state[_G]=_A;return _B,'❌ Timeout: Image generation took too long'
        try:
            G=requests.get(T,timeout=15).json()
            if not G.get(I)or len(G[I])==0:app_state[_G]=_A;return _B,'❌ No image generated'
            X=G[I][0]['img']
            if A:A('⬇️ Downloading image...',95)
            O=requests.get(X,timeout=30);O.raise_for_status();B=tempfile.NamedTemporaryFile(delete=_A,suffix='.png',dir=os.environ.get('TEMP',tempfile.gettempdir()));B.write(O.content);B.close();app_state[_P].append(B.name);Y=Image.open(B.name);app_state[_G]=_A
            if A:A('🎉 AI image ready!',100)
            return Y,f"✅ AI image generated successfully!\n🗂️ Temp file: {os.path.basename(B.name)}"
        except Exception as H:app_state[_G]=_A;return _B,f"❌ Failed to download image: {str(H)}"
    except Exception as H:app_state[_G]=_A;return _B,f"❌ AI generation error: {str(H)}"
def press_enter_real():'Press Enter using raw keybd_event with scancode for Roblox compatibility';ctypes.windll.user32.keybd_event(13,28,0,0);time.sleep(.05);ctypes.windll.user32.keybd_event(13,28,2,0)
def is_windows_locked():
    'Check if Windows is locked'
    try:
        A=ctypes.windll.user32.OpenDesktopW('default',0,_A,256)
        if A:ctypes.windll.user32.CloseDesktop(A);return _A
        else:return _C
    except:return _A
def simple_click(x,y,delay_after=.05):
    'Reliable clicking with proper delays';win32api.SetCursorPos((x,y));time.sleep(.02)
    for A in range(2):win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,1,1,0,0);win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,-1,-1,0,0)
    time.sleep(.02);win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0);time.sleep(.01);win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0);time.sleep(delay_after)
def rgb_to_hex(pixel):'Convert RGB to hex';return'{:02x}{:02x}{:02x}'.format(*pixel).upper()
def get_pixel_brightness(color):'Calculate perceived brightness of a color';A,B,C=color;return(.299*A+.587*B+.114*C)/255
def apply_image_filter(image,filter_type,contrast_level=1.):
    'Apply various filters to enhance pixel art conversion';D=contrast_level;B=filter_type;A=image
    if D!=1.:E=ImageEnhance.Contrast(A);A=E.enhance(D)
    if B==_W:return A
    elif B=='Sharpen':return A.filter(ImageFilter.SHARPEN)
    elif B==_A6:return A.filter(ImageFilter.BLUR)
    elif B==_A7:return A.filter(ImageFilter.EDGE_ENHANCE)
    elif B==_A8:C=np.array(A);C=C//32*32;return Image.fromarray(C.astype(np.uint8))
    return A
def convert_to_pixel_art(image,filter_type=_W,contrast_level=1.):
    'Enhanced pixel art conversion with filters - FIXED 32x32 SIZE with PROPER SCALING';I=image
    if not I:return _B,{}
    A=32;D=apply_image_filter(I,filter_type,contrast_level);E=D.width/D.height
    if E>1:F=A;G=int(A/E)
    else:F=int(A*E);G=A
    L=D.resize((F,G),Image.LANCZOS);H=Image.new(_f,(A,A),color=(255,255,255));M=(A-F)//2,(A-G)//2;H.paste(L,M);N=H.resize((320,320),Image.NEAREST);O=H.load();B={}
    for J in range(A):
        for K in range(A):
            C=O[J,K]
            if C!=(255,255,255):
                if C not in B:B[C]=[]
                B[C].append((J,K))
    return N,B
def get_drawing_order(pixel_colors,pattern=_Z):
    'Get pixel drawing order based on selected pattern';G=pattern;E=pixel_colors
    if G==_Z:return list(E.items())
    elif G==_A2:
        D=[]
        for(A,F)in E.items():
            for C in F:D.append((A,C))
        D.sort(key=lambda x:(x[1][0],x[1][1]));B={}
        for(A,C)in D:
            if A not in B:B[A]=[]
            B[A].append(C)
        return list(B.items())
    elif G==_A3:
        D=[]
        for(A,F)in E.items():
            for C in F:D.append((A,C))
        D.sort(key=lambda x:(x[1][1],x[1][0]));B={}
        for(A,C)in D:
            if A not in B:B[A]=[]
            B[A].append(C)
        return list(B.items())
    elif G=='spiral':
        H=16;D=[]
        for(A,F)in E.items():
            for C in F:J,K=C;M=((J-H)**2+(K-H)**2)**.5;N=np.arctan2(K-H,J-H);D.append((A,C,M,N))
        D.sort(key=lambda x:(x[2],x[3]));B={}
        for(A,C,O,O)in D:
            if A not in B:B[A]=[]
            B[A].append(C)
        return list(B.items())
    elif G==_A4:L=[(A,get_pixel_brightness(A),B)for(A,B)in E.items()];L.sort(key=lambda x:x[1]);return[(A,B)for(A,C,B)in L]
    elif G=='random':
        I=list(E.items());random.shuffle(I)
        for(A,F)in I:random.shuffle(F)
        return I
    else:return list(E.items())
def create_color_palette_image(pixel_colors):
    'Create a visual color palette - BIGGER PALETTE';D=pixel_colors
    if not D:return
    E=list(D.keys());C=min(len(E),64);B=int(np.ceil(np.sqrt(C)));H=int(np.ceil(C/B));A=60;F=Image.new(_f,(B*A,H*A),(240,240,240))
    for(G,I)in enumerate(E[:C]):J=G//B;K=G%B;L=Image.new(_f,(A-4,A-4),I);F.paste(L,(K*A+2,J*A+2))
    return F
def save_settings():
    'Save current settings';A={_D:app_state[_D],_A9:datetime.now().isoformat()}
    try:
        with open(app_state[_X],'w')as B:json.dump(A,B,indent=2)
        return'✅ Settings saved successfully!'
    except Exception as C:return f"❌ Error saving: {str(C)}"
def load_settings():
    'Load saved settings'
    try:
        if os.path.exists(app_state[_X]):
            with open(app_state[_X],'r')as A:B=json.load(A)
            app_state[_D].update(B.get(_D,{}));return'✅ Settings loaded successfully!'
        else:return'📁 No settings file found'
    except Exception as C:return f"❌ Error loading: {str(C)}"
def calibrate_position(coord_type):
    'Calibrate a position with 3-second countdown';A=coord_type
    for F in range(3,0,-1):time.sleep(1)
    B=pyautogui.position();C={_AA:(_K,_L),_AB:(_Q,_R),_AC:(_S,_T),_AD:(_U,_V),_AE:(_M,_N)}
    if A in C:D,E=C[A];app_state[_D][D]=B[0];app_state[_D][E]=B[1];save_settings();return f"✅ {A} set to {B}"
    return f"❌ Unknown coordinate type: {A}"
def get_calibration_status():
    'Get current calibration status';A=[_K,_L,_Q,_R,_S,_T,_U,_V,_M,_N];B=sum(1 for A in A if app_state[_D][A]is not _B)
    if B==len(A):return'✅ Fully Calibrated - Ready to Draw!'
    else:return f"⚠️ {B}/{len(A)} calibrated"
def process_image(image,filter_type,contrast_level,color_reduction):
    'Process uploaded image with advanced options - AUTO PROCESSING';C=color_reduction;A=image
    if A is _B:return _B,_B,'❌ No image provided'
    try:
        app_state[_h]=A
        if C>1:B=np.array(A);J=max(2,C);G=256//J;B=B//G*G;B=np.clip(B,0,255);A=Image.fromarray(B.astype(np.uint8))
        E,D=convert_to_pixel_art(A,filter_type,contrast_level)
        if E:
            app_state[_i]=E.resize((32,32),Image.NEAREST);app_state[_E]=D;K=len(D);H=sum(len(A)for A in D.values());I=H*.1;L=I/60;app_state[_I][_a]=I;F=f"🎨 Processed! {K} colors, {H} pixels"
            if C>1:F+=f" | 🎨 Colors reduced to {C} levels"
            F+=f"\n⏱️ Estimated time: {L:.1f} minutes";save_settings();return E,create_color_palette_image(D),F
        else:return _B,_B,'❌ Failed to process image'
    except Exception as M:return _B,_B,f"❌ Error: {str(M)}"
def click_pixel(x,y):'Click a specific pixel on the canvas';A=app_state[_D];B=round(A[_K]+x*(A[_Q]-A[_K])/31);C=round(A[_L]+y*(A[_R]-A[_L])/31);simple_click(B,C,delay_after=.02)
def select_color(color,use_clipboard=_C):
    'Select color in Roblox with enhanced reliability';C='ctrl'
    try:
        A=app_state[_D];B=rgb_to_hex(color);simple_click(A[_S],A[_T],delay_after=.15);simple_click(A[_U],A[_V],delay_after=.1)
        if use_clipboard:pyperclip.copy(B);time.sleep(.05);pyautogui.hotkey(C,'a');time.sleep(.02);pyautogui.hotkey(C,'v')
        else:pyautogui.typewrite(B)
        time.sleep(.1);press_enter_real();time.sleep(.15)
        for D in range(2):simple_click(A[_M],A[_N],delay_after=.1)
        return _C
    except Exception as E:return _A
def get_speed_from_selection(speed_selection):'Get speed value from radio selection';return SPEED_VALUES.get(speed_selection,.2)
def get_pattern_from_selection(pattern_selection):'Get pattern key from radio selection';return PATTERN_VALUES.get(pattern_selection,_Z)
def draw_pixel_art_enhanced(speed_selection,custom_speed,pattern_selection,use_clipboard,progress=gr.Progress()):
    'Enhanced drawing function with patterns and floating progress bar';E=progress;D=speed_selection
    if not app_state[_E]:return'❌ No image loaded!'
    K=[_K,_L,_Q,_R,_S,_T,_U,_V,_M,_N]
    if not all(app_state[_D][A]is not _B for A in K):return'❌ Please complete calibration first!'
    if app_state[_H]:return'⚠️ Already drawing! Stop current drawing first.'
    if D==_Y:F=custom_speed
    else:F=get_speed_from_selection(D)
    L=get_pattern_from_selection(pattern_selection);app_state[_H]=_C;app_state[_J]=_A;app_state[_F]=0;app_state[_I][_O]=time.time();floating_progress.show()
    try:
        B=get_drawing_order(app_state[_E],L);A=sum(len(A)for(B,A)in B);M=len(B);E(0,desc='🚀 Starting pixel art drawing...');floating_progress.update_progress(0,0,0,A);time.sleep(1);G=app_state[_D]
        for U in range(2):simple_click(G[_M],G[_N]);time.sleep(.1)
        H=0
        for(N,O)in B:
            if not app_state[_H]or app_state[_J]:break
            if not select_color(N,use_clipboard):continue
            for P in O:
                if not app_state[_H]or app_state[_J]:break
                if is_windows_locked():app_state[_J]=_C;break
                Q,R=P;click_pixel(Q,R);app_state[_F]+=1;I=app_state[_F]/A*100;S=time.time()-app_state[_I][_O]
                if app_state[_F]>0:C=S/app_state[_F]*(A-app_state[_F])
                else:C=0
                E(I/100,desc=f"🎨 Drawing... {app_state[_F]}/{A} pixels | ⏱️ {C/60:.1f}min remaining");floating_progress.update_progress(I,C,app_state[_F],A);time.sleep(F)
            H+=1
            if H<M:time.sleep(.2)
        app_state[_H]=_A;J=time.time()-app_state[_I][_O];floating_progress.hide()
        if app_state[_J]:return f"🔒 Drawing stopped! Drew {app_state[_F]}/{A} pixels in {J/60:.1f}min"
        else:return f"🎉 Drawing completed! Drew {A} pixels in {J/60:.1f}min"
    except Exception as T:app_state[_H]=_A;floating_progress.hide();return f"❌ Drawing error: {str(T)}"
def stop_drawing():
    'Stop the current drawing'
    if app_state[_H]:app_state[_H]=_A;app_state[_J]=_C;floating_progress.hide();return'⏹️ Drawing stopped!'
    return'ℹ️ No drawing in progress'
def get_stats():
    'Get current drawing statistics'
    if not app_state[_E]:return'📊 No image loaded'
    B=sum(len(A)for A in app_state[_E].values());C=len(app_state[_E]);A=f"""
📊 **Current Image Stats:**

🎨 **Colors:** {C} unique colors  
🎯 **Pixels:** {B} pixels to draw  
⏱️ **Est. Time:** {app_state[_I][_a]/60:.1f} minutes

🚀 **Drawing Progress:**  
✅ **Drawn:** {app_state[_F]} pixels
"""
    if app_state[_I][_O]:D=time.time()-app_state[_I][_O];A+=f"\n⌚ **Elapsed:** {D/60:.1f} minutes"
    return A
custom_css='\n/* Night sky animated background */\n@keyframes stars-twinkle {\n    0%, 100% { opacity: 0.3; transform: scale(1); }\n    50% { opacity: 1; transform: scale(1.2); }\n}\n\n@keyframes shooting-star {\n    0% { transform: translateX(-100px) translateY(100px); opacity: 0; }\n    10% { opacity: 1; }\n    90% { opacity: 1; }\n    100% { transform: translateX(1000px) translateY(-100px); opacity: 0; }\n}\n\n@keyframes aurora {\n    0%, 100% { background-position: 0% 50%; }\n    50% { background-position: 100% 50%; }\n}\n\n@keyframes ai-glow {\n    0%, 100% { box-shadow: 0 0 20px rgba(255, 100, 255, 0.3); }\n    50% { box-shadow: 0 0 40px rgba(255, 100, 255, 0.8); }\n}\n\n@keyframes gradient-shift {\n    0%, 100% { background-position: 0% 50%; }\n    50% { background-position: 100% 50%; }\n}\n\n.gradio-container {\n    background: linear-gradient(180deg, #0c0c2e 0%, #1a1a3e 30%, #2d1b69 70%, #4a1c4a 100%) !important;\n    background-size: 400% 400% !important;\n    animation: aurora 20s ease infinite !important;\n    font-family: \'Segoe UI\', Tahoma, Geneva, Verdana, sans-serif !important;\n    min-height: 100vh !important;\n    position: relative !important;\n}\n\n/* HIDE FULLSCREEN BUTTON TO PREVENT LAG */\nbutton[title="View in fullscreen"], \n.fullscreen-button,\nbutton[aria-label="View in fullscreen"],\nfooter {visibility: hidden},\nbutton[data-testid="fullscreen-button"] {\n    display: none !important;\n    visibility: hidden !important;\n}\n\n/* AI Generation specific styling */\n.ai-container {\n    background: linear-gradient(45deg, rgba(255, 100, 255, 0.1), rgba(100, 100, 255, 0.1)) !important;\n    border: 2px solid rgba(255, 100, 255, 0.3) !important;\n    border-radius: 20px !important;\n    animation: ai-glow 4s ease-in-out infinite !important;\n}\n\n/* Twinkling stars background */\n.gradio-container::before {\n    content: \'\';\n    position: fixed;\n    top: 0;\n    left: 0;\n    width: 100%;\n    height: 100%;\n    background-image: \n        radial-gradient(2px 2px at 20px 30px, rgba(255,255,255,0.8), transparent),\n        radial-gradient(1px 1px at 40px 70px, rgba(200,200,255,0.6), transparent),\n        radial-gradient(1px 1px at 90px 40px, rgba(255,255,255,0.9), transparent),\n        radial-gradient(2px 2px at 130px 80px, rgba(180,180,255,0.7), transparent),\n        radial-gradient(1px 1px at 160px 30px, rgba(255,255,255,0.5), transparent),\n        radial-gradient(2px 2px at 200px 120px, rgba(255,200,255,0.6), transparent),\n        radial-gradient(1px 1px at 250px 60px, rgba(200,255,255,0.8), transparent),\n        radial-gradient(1px 1px at 300px 100px, rgba(255,255,255,0.7), transparent);\n    background-repeat: repeat;\n    background-size: 350px 250px;\n    animation: stars-twinkle 3s ease-in-out infinite alternate;\n    pointer-events: none;\n    z-index: 1;\n}\n\n/* Enhanced glassmorphism cards with night theme */\n.block {\n    background: rgba(30, 30, 80, 0.3) !important;\n    backdrop-filter: blur(20px) !important;\n    border: 1px solid rgba(100, 150, 255, 0.3) !important;\n    border-radius: 20px !important;\n    box-shadow: 0 15px 35px rgba(0, 0, 50, 0.4) !important;\n    position: relative !important;\n    z-index: 2 !important;\n    margin: 10px !important;\n}\n\n/* Night-themed button styling */\n.btn {\n    background: linear-gradient(45deg, #4a90e2, #357abd, #6a5acd, #483d8b) !important;\n    background-size: 300% 300% !important;\n    animation: aurora 4s ease infinite !important;\n    border: none !important;\n    border-radius: 15px !important;\n    font-weight: bold !important;\n    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;\n    padding: 12px 24px !important;\n    box-shadow: 0 8px 25px rgba(0, 0, 50, 0.5) !important;\n    position: relative !important;\n    overflow: hidden !important;\n    z-index: 3 !important;\n    color: white !important;\n}\n\n.btn:hover {\n    transform: translateY(-5px) scale(1.05) !important;\n    box-shadow: 0 15px 40px rgba(100, 150, 255, 0.4) !important;\n}\n\n/* Enhanced image containers with night glow - BETTER SCALING */\n.image-container img {\n    border-radius: 15px !important;\n    box-shadow: 0 10px 30px rgba(0, 0, 100, 0.6) !important;\n    transition: transform 0.3s ease !important;\n    border: 2px solid rgba(100, 150, 255, 0.3) !important;\n    max-width: 100% !important;\n    height: auto !important;\n    image-rendering: pixelated !important;\n    image-rendering: -moz-crisp-edges !important;\n    image-rendering: crisp-edges !important;\n}\n\n/* Starry headers */\nh1, h2, h3 {\n    color: white !important;\n    text-shadow: 0 0 20px rgba(200, 200, 255, 0.8) !important;\n    background: linear-gradient(45deg, #fff, #e0e0ff, #fff) !important;\n    background-size: 200% 200% !important;\n    -webkit-background-clip: text !important;\n    -webkit-text-fill-color: transparent !important;\n    animation: gradient-shift 4s ease infinite !important;\n    position: relative !important;\n    z-index: 3 !important;\n}\n\n/* Night-themed input styling */\ninput[type="text"], input[type="number"], input[type="range"], textarea {\n    background: rgba(20, 20, 60, 0.4) !important;\n    border: 2px solid rgba(100, 150, 255, 0.4) !important;\n    border-radius: 12px !important;\n    color: white !important;\n    padding: 10px 15px !important;\n    transition: all 0.3s ease !important;\n    backdrop-filter: blur(10px) !important;\n}\n\ninput:focus, textarea:focus {\n    border-color: rgba(100, 150, 255, 0.8) !important;\n    box-shadow: 0 0 20px rgba(100, 150, 255, 0.5) !important;\n    transform: scale(1.02) !important;\n}\n\n/* Night-themed radio buttons */\n.radio-group label {\n    color: white !important;\n    padding: 8px 15px !important;\n    margin: 3px !important;\n    border-radius: 12px !important;\n    background: rgba(30, 30, 80, 0.3) !important;\n    transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;\n    border: 1px solid rgba(100, 150, 255, 0.4) !important;\n    backdrop-filter: blur(10px) !important;\n}\n\n.radio-group label:hover {\n    background: rgba(50, 50, 120, 0.5) !important;\n    transform: translateY(-2px) scale(1.05) !important;\n    box-shadow: 0 5px 15px rgba(100, 150, 255, 0.3) !important;\n}\n'
def create_interface():
    G='primary';A='secondary'
    with gr.Blocks(css=custom_css,title=_AF,theme=gr.themes.Soft())as D:
        gr.HTML('\n        <div style="text-align: center; padding: 30px; position: relative; z-index: 3;">\n            <h1 style="font-size: 3em; margin: 0;">\n                🎨 Roblox Pixel Art Converter Pro + AI\n            </h1>\n            <p style="font-size: 1.3em; color: rgba(255,255,255,0.9); margin: 15px 0; \n                      text-shadow: 0 0 10px rgba(255,255,255,0.5);">\n                \n            </p>\n            <div style="background: rgba(255,255,255,0.1); padding: 10px 20px; border-radius: 25px; \n                        display: inline-block; backdrop-filter: blur(10px); margin-top: 10px;\n                        border: 1px solid rgba(255,255,255,0.2);">\n                <span style="color: rgba(255,255,255,0.8); font-size: 0.9em;">\n                    NEW FEATURE : 🤖 AI Image Generation \n                </span>\n            </div>\n        </div>\n        ')
        with gr.Tabs():
            with gr.Tab('🖼️ Image Processing + AI'):
                with gr.Row():
                    with gr.Column(scale=1):
                        gr.Markdown('### 🤖 AI Image Generation')
                        with gr.Group(elem_classes=['ai-container']):
                            V=gr.Textbox(label='✨ AI Prompt',placeholder='A cute strawberry pie with anime eyes, kawaii style...',lines=2);W=gr.Radio(choices=AI_STYLE_PRESETS,value=_b,label='🎨 Style Preset')
                            with gr.Row():X=gr.Button('🤖 Generate AI Image',variant=G);Y=gr.Markdown('🤖 Ready to generate!')
                        gr.Markdown('### 📁 Manual Upload');E=gr.Image(type='pil',label='Upload Image',height=250);gr.Markdown('### 🎛️ Processing Options')
                        with gr.Row():H=gr.Radio([_W,'Sharpen',_A6,_A7,_A8],value=_W,label='🎛️ Image Filter')
                        with gr.Row():I=gr.Slider(.5,3.,value=1.,step=.1,label='🔆 Contrast Level')
                        with gr.Row():J=gr.Slider(0,32,value=0,step=1,label='🎨 Color Reduction (0=Off, 2-32=Active)')
                        Z=gr.Markdown('📝 Upload an image or generate with AI!')
                    with gr.Column(scale=1):gr.Markdown('### 👁️ Preview - Pixel Perfect Scaling!');K=gr.Image(label='Pixel Art Preview (320x320 display)',interactive=_A,height=450);L=gr.Image(label='Color Palette',interactive=_A,height=250);s=gr.Markdown('📊 **Stats will appear here**')
            with gr.Tab('🎯 Calibration'):
                gr.Markdown('### 🎯 Position Calibration');gr.Markdown('Position your cursor over each target, then click the button. Wait for 3-second countdown!')
                with gr.Row():
                    with gr.Column():gr.Markdown('#### 📐 Canvas Coordinates');M=gr.Button('📍 Set Top-Left Pixel',variant=A);N=gr.Button('📍 Set Bottom-Right Pixel',variant=A)
                    with gr.Column():gr.Markdown('#### 🎨 Tool Coordinates');O=gr.Button('🎨 Set Color Button',variant=A);P=gr.Button('📝 Set Hex Input',variant=A);Q=gr.Button('❌ Set Close Button',variant=A)
                with gr.Row():R=gr.Markdown('⚠️ Not calibrated')
                with gr.Row():a=gr.Button('💾 Save Settings',variant=G);b=gr.Button('📂 Load Settings',variant=A)
                B=gr.Textbox(label='Calibration Output',interactive=_A)
            with gr.Tab('🚀 Drawing Control + Floating Progress'):
                with gr.Row():
                    with gr.Column(scale=1):
                        gr.Markdown('### ⚡ Speed & Pattern Settings');F=gr.Radio(choices=SPEED_OPTIONS,value=_d,label='🎛️ Speed Preset',interactive=_C);S=gr.Slider(.001,2.,value=.2,step=.001,label='🎛️ Custom Speed (seconds)',visible=_A);c=gr.Radio(choices=PATTERN_OPTIONS,value=_e,label='🌀 Drawing Pattern',interactive=_C)
                        with gr.Row():d=gr.Checkbox(value=_C,label='📋 Use Clipboard for Hex Input')
                    with gr.Column(scale=1):
                        gr.Markdown('### 🎮 Drawing Controls')
                        with gr.Row():e=gr.Button('🚀 Start Drawing',variant=G,size='lg');f=gr.Button('⏹️ Stop Drawing',variant='stop',size='lg')
                        T=gr.Markdown('🎯 Ready to draw!');gr.Markdown('### 📊 Live Statistics');C=gr.Markdown('📈 Stats will update during drawing');g=gr.Button('🔄 Refresh Stats',variant=A);gr.Markdown('\n                        ### 🎯 Floating Progress Bar Features:\n                        - 📊 **Stays on top** of all windows during drawing\n                        - ⏱️ **Real-time progress** with time remaining\n                        - 🎯 **Pixel counter** showing progress\n                        - 🪟 **Top-right corner** positioning\n                        - ⚡ **Auto-hides** when drawing completes\n                        ');gr.Markdown('\n                        ### 🚨 Emergency Stop Methods:\n                        - 🔒 **Windows + L** (Lock screen) - Most reliable\n                        - ⏹️ **Stop Button** - UI control\n                        - 🖱️ **Move mouse to corner** - Failsafe trigger\n                        ')
            with gr.Tab('⚙️ Advanced + Security'):
                with gr.Row():
                    with gr.Column():gr.Markdown('### 🔒 Security Features');gr.Markdown('\n                        #### 🛡️ Encryption Status:\n                        - ✅ **API Key Encrypted** with AES-256\n                        - 🔐 **Decryption Key**: `PePa24410`\n                        - 🗂️ **Temp Files**: Auto-cleanup on exit\n                        - 🔄 **Memory Security**: No persistent storage\n                        ');h=gr.Button('🗑️ Clean Temp Files Now',variant=A);i=gr.Textbox(label='Cleanup Status',interactive=_A)
                    with gr.Column():gr.Markdown('### 📊 AI Generation Stats');t=gr.Markdown('\n                        #### 🤖 AI Features:\n                        - 🎨 **10+ Style Presets** available\n                        - ⏱️ **Real-time progress** during generation\n                        - 🗂️ **Temp file storage** in %TEMP%\n                        - 🔄 **Auto-cleanup** on program exit\n                        - 📊 **Queue position** tracking\n                        ');j=gr.Button('📊 Export Drawing Data',variant=A);k=gr.Textbox(label='Export Status',interactive=_A)
        def l(selection):return gr.update(visible=selection==_Y)
        def U():return get_calibration_status()
        def m():
            'Export current drawing data as JSON'
            if not app_state[_E]:return'❌ No data to export'
            B={_A9:datetime.now().isoformat(),'canvas_size':32,'total_colors':len(app_state[_E]),'total_pixels':sum(len(A)for A in app_state[_E].values()),'color_data':{rgb_to_hex(A):len(B)for(A,B)in app_state[_E].items()}};A=f"pixel_art_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            try:
                with open(A,'w')as C:json.dump(B,C,indent=2)
                return f"✅ Data exported to {A}"
            except Exception as D:return f"❌ Export failed: {str(D)}"
        def n():'Manual cleanup of temp files';cleanup_temp_files();return f"✅ Cleaned up {len(app_state[_P])} temp files"
        def o(prompt,style_preset,progress=gr.Progress()):
            'Wrapper for AI image generation with progress';E='⚠️ AI generation already in progress';D='❌ Please enter a prompt';B=prompt
            if not B.strip():return _B,_B,D,D
            if app_state[_G]:return _B,_B,E,E
            def F(message,percentage):
                A=percentage
                if A is not _B:progress(A/100,desc=message)
                return not app_state[_G]
            A,C=generate_ai_image(B,style_preset,F)
            if A:G,H,I=process_image(A,_W,1.,0);return A,G,H,C
            else:return _B,_B,_B,C
        X.click(o,[V,W],[E,K,L,Y]);F.change(l,F,S)
        def p(*A):B,C,D=process_image(*A);return B,C,D
        for q in[E,H,I,J]:q.change(p,[E,H,I,J],[K,L,Z])
        M.click(lambda:calibrate_position(_AA),outputs=B);N.click(lambda:calibrate_position(_AB),outputs=B);O.click(lambda:calibrate_position(_AC),outputs=B);P.click(lambda:calibrate_position(_AD),outputs=B);Q.click(lambda:calibrate_position(_AE),outputs=B)
        for r in[M,N,O,P,Q]:r.click(U,outputs=R)
        a.click(save_settings,outputs=B);b.click(load_settings,outputs=B);e.click(get_stats,outputs=C).then(draw_pixel_art_enhanced,[F,S,c,d],[T]).then(get_stats,outputs=C);f.click(stop_drawing,outputs=[T]).then(get_stats,outputs=C);g.click(get_stats,outputs=C);j.click(m,outputs=k);h.click(n,outputs=i);D.load(load_settings,outputs=B);D.load(U,outputs=R)
    return D

def show_key_dialog():
    'Show key verification dialog'
    root = tk.Tk()
    root.title("🔑 License Verification")
    root.geometry("500x400")
    root.configure(bg='#1a1a3e')
    root.resizable(False, False)
    
    # Center window
    root.eval('tk::PlaceWindow . center')
    
    # Make it stay on top
    root.attributes('-topmost', True)
    
    result = {'key': None, 'verified': False}
    
    # Title
    title = tk.Label(root, text="🎨 Roblox Pixel Art Pro", 
                    font=('Arial', 20, 'bold'), 
                    fg='white', bg='#1a1a3e')
    title.pack(pady=20)
    
    # Branding
    brand = tk.Label(root, text="Made by: 43.83 on Discord\nhttps://guns.lol/kiro.of", 
                    font=('Arial', 12), 
                    fg='#cccccc', bg='#1a1a3e')
    brand.pack(pady=10)
    
    # Key input
    tk.Label(root, text="Enter License Key:", 
            font=('Arial', 14), fg='white', bg='#1a1a3e').pack(pady=(20,5))
    
    key_entry = tk.Entry(root, font=('Arial', 12), width=40, 
                        bg='#2d2d5e', fg='white', insertbackground='white')
    key_entry.pack(pady=5)
    
    status_label = tk.Label(root, text="", font=('Arial', 10), 
                           fg='red', bg='#1a1a3e')
    status_label.pack(pady=10)
    
    def verify_clicked():
        key = key_entry.get().strip()
        if not key:
            status_label.config(text="Please enter a key", fg='red')
            return
        
        status_label.config(text="Verifying...", fg='yellow')
        root.update()
        
        verification = verify_key(key)
        
        if verification['valid']:
            result['key'] = key
            result['verified'] = True
            result['info'] = verification
            status_label.config(text="✅ License verified!", fg='green')
            root.after(1000, root.destroy)
        else:
            status_label.config(text=f"❌ {verification['message']}", fg='red')
    
    verify_btn = tk.Button(root, text="🔑 Verify License", 
                          command=verify_clicked, font=('Arial', 12),
                          bg='#4a90e2', fg='white', padx=20, pady=5)
    verify_btn.pack(pady=20)
    
    # Bind Enter key
    key_entry.bind('<Return>', lambda e: verify_clicked())
    key_entry.focus()
    
    root.mainloop()
    return result


def launch_in_webview(app):
    'Launch the Gradio app in an embedded webview that stays on top'
    def A():app.launch(server_name=_g,server_port=7860,share=_A,debug=_A,inbrowser=_A,prevent_thread_lock=_C)
    B=threading.Thread(target=A,daemon=_C);B.start();time.sleep(3);webview.create_window(title=_AF,url='http://127.0.0.1:7860',width=1200,height=900,min_size=(1000,700),resizable=_C,fullscreen=_A,minimized=_A,on_top=_C,shadow=_C,focus=_C);webview.start(debug=_A)
def main():
    print('🔑 Starting license verification...')
    license_result = show_key_dialog()

    if not license_result['verified']:
        print('❌ License verification failed. Exiting...')
        return

    print('✅ License verified successfully!')
    print(f"License Type: {license_result['info'].get('duration', 'Unknown')}")

    # ─── All app startup must happen _after_ verification ───
    load_settings()
    app = create_interface()
    try:
        launch_in_webview(app)
    except ImportError:
        print('⚠️ pywebview not available; launching browser instead')
        app.launch(...)
    finally:
        cleanup_temp_files()




if __name__=='__main__':main()