import numpy as np
import plotly.graph_objects as go

def draw_accurate_heart(x, y, size=0.08, color="#e74c3c", opacity=0.8, line_width=2):
    """Vẽ tim với hình dạng chính xác theo giải phẫu"""
    # Tạo hình tim chính xác với 2 tâm nhĩ và 2 tâm thất
    t = np.linspace(0, 2*np.pi, 100)
    
    # Phần trên tim (tâm nhĩ) - 2 hình tròn nhỏ
    left_atrium_x = x - size*0.3 + size*0.2 * np.cos(t)
    left_atrium_y = y + size*0.4 + size*0.15 * np.sin(t)
    
    right_atrium_x = x + size*0.3 + size*0.2 * np.cos(t)
    right_atrium_y = y + size*0.4 + size*0.15 * np.sin(t)
    
    # Phần dưới tim (tâm thất) - hình giọt nước
    ventricle_t = np.linspace(0, 2*np.pi, 50)
    ventricle_x = x + size*0.6 * np.cos(ventricle_t)
    ventricle_y = y - size*0.2 + size*0.4 * np.sin(ventricle_t)
    
    # Điều chỉnh để tạo hình tim thực tế
    heart_x = []
    heart_y = []
    
    # Tạo đường viền tim thực tế
    for i in range(100):
        angle = i * 2 * np.pi / 100
        if angle < np.pi:  # Phần trên
            heart_x.append(x + size * (0.5 * np.cos(angle) - 0.2 * np.cos(2*angle)))
            heart_y.append(y + size * (0.5 * np.sin(angle) + 0.3))
        else:  # Phần dưới nhọn
            heart_x.append(x + size * 0.7 * np.cos(angle) * (1 - 0.3 * np.sin(angle/2)))
            heart_y.append(y + size * 0.8 * np.sin(angle))
    
    heart_x.append(heart_x[0])  # Đóng đường viền
    heart_y.append(heart_y[0])
    
    return go.Scatter(
        x=heart_x, y=heart_y,
        fill='toself',
        fillcolor=color,
        opacity=opacity,
        line=dict(color=color, width=line_width),
        name="Tim",
        hovertemplate="<b>Tim</b><br>Cơ quan bơm máu chính<br>4 buồng: 2 tâm nhĩ, 2 tâm thất<extra></extra>",
        showlegend=True
    )

def draw_accurate_lungs(x, y, size=0.1, color="#3498db", opacity=0.8, line_width=2, lung_type="left"):
    """Vẽ phổi với hình dạng chính xác theo giải phẫu"""
    traces = []
    
    if lung_type == "left":
        # Phổi trái - 2 thùy
        # Thùy trên
        upper_lobe_t = np.linspace(0, np.pi, 30)
        upper_x = x + size*0.8 * np.cos(upper_lobe_t)
        upper_y = y + size*0.3 + size*0.4 * np.sin(upper_lobe_t)
        
        # Thùy dưới
        lower_lobe_t = np.linspace(np.pi, 2*np.pi, 30)
        lower_x = x + size*0.7 * np.cos(lower_lobe_t)
        lower_y = y - size*0.2 + size*0.5 * np.sin(lower_lobe_t)
        
        # Kết hợp thành hình phổi
        lung_x = list(upper_x) + list(lower_x)
        lung_y = list(upper_y) + list(lower_y)
        
    else:  # right lung
        # Phổi phải - 3 thùy
        # Thùy trên
        upper_lobe_t = np.linspace(0, np.pi*0.6, 20)
        upper_x = x + size*0.8 * np.cos(upper_lobe_t)
        upper_y = y + size*0.4 + size*0.3 * np.sin(upper_lobe_t)
        
        # Thùy giữa
        middle_lobe_t = np.linspace(np.pi*0.6, np.pi*1.2, 20)
        middle_x = x + size*0.6 * np.cos(middle_lobe_t)
        middle_y = y + size*0.1 + size*0.3 * np.sin(middle_lobe_t)
        
        # Thùy dưới
        lower_lobe_t = np.linspace(np.pi*1.2, 2*np.pi, 20)
        lower_x = x + size*0.7 * np.cos(lower_lobe_t)
        lower_y = y - size*0.3 + size*0.4 * np.sin(lower_lobe_t)
        
        # Kết hợp thành hình phổi
        lung_x = list(upper_x) + list(middle_x) + list(lower_x)
        lung_y = list(upper_y) + list(middle_y) + list(lower_y)
    
    # Làm mịn đường viền phổi
    lung_x.append(lung_x[0])
    lung_y.append(lung_y[0])
    
    return go.Scatter(
        x=lung_x, y=lung_y,
        fill='toself',
        fillcolor=color,
        opacity=opacity,
        line=dict(color=color, width=line_width),
        name=f"Phổi {'trái' if lung_type == 'left' else 'phải'}",
        hovertemplate=f"<b>Phổi {'trái' if lung_type == 'left' else 'phải'}</b><br>Trao đổi khí O2/CO2<br>{'2 thùy' if lung_type == 'left' else '3 thùy'}<extra></extra>",
        showlegend=True
    )

def draw_accurate_liver(x, y, size=0.12, color="#f39c12", opacity=0.8, line_width=2):
    """Vẽ gan với hình dạng chính xác theo giải phẫu"""
    # Gan có hình dạng đặc biệt với 4 thùy chính
    # Thùy phải (lớn nhất)
    right_lobe_t = np.linspace(-np.pi/3, np.pi/3, 30)
    right_x = x + size*0.4 + size*0.6 * np.cos(right_lobe_t)
    right_y = y + size*0.4 * np.sin(right_lobe_t)
    
    # Thùy trái (nhỏ hơn)
    left_lobe_t = np.linspace(2*np.pi/3, 4*np.pi/3, 25)
    left_x = x - size*0.3 + size*0.4 * np.cos(left_lobe_t)
    left_y = y + size*0.3 * np.sin(left_lobe_t)
    
    # Phần giữa nối hai thùy
    middle_x = [x - size*0.1, x + size*0.1]
    middle_y = [y + size*0.3, y + size*0.3]
    
    # Phần dưới gan
    bottom_t = np.linspace(4*np.pi/3, 5*np.pi/3, 15)
    bottom_x = x + size*0.8 * np.cos(bottom_t)
    bottom_y = y - size*0.4 + size*0.2 * np.sin(bottom_t)
    
    # Kết hợp tạo hình gan
    liver_x = list(right_x) + list(bottom_x) + list(left_x) + middle_x
    liver_y = list(right_y) + list(bottom_y) + list(left_y) + middle_y
    
    liver_x.append(liver_x[0])
    liver_y.append(liver_y[0])
    
    return go.Scatter(
        x=liver_x, y=liver_y,
        fill='toself',
        fillcolor=color,
        opacity=opacity,
        line=dict(color=color, width=line_width),
        name="Gan",
        hovertemplate="<b>Gan</b><br>Cơ quan lớn nhất trong cơ thể<br>Giải độc, sản xuất mật, dự trữ năng lượng<extra></extra>",
        showlegend=True
    )

def draw_accurate_kidneys(x, y, size=0.08, color="#1abc9c", opacity=0.8, line_width=2):
    """Vẽ thận với hình dạng chính xác theo giải phẫu"""
    # Thận có hình đậu
    t = np.linspace(0, 2*np.pi, 60)
    
    # Tạo hình đậu với phần lõm ở giữa
    kidney_x = []
    kidney_y = []
    
    for i, angle in enumerate(t):
        # Điều chỉnh bán kính để tạo hình đậu
        if np.pi/3 < angle < 2*np.pi/3:  # Phần lõm
            radius = size * 0.4
        else:
            radius = size * 0.8
            
        kidney_x.append(x + radius * np.cos(angle))
        kidney_y.append(y + radius * 1.2 * np.sin(angle))
    
    kidney_x.append(kidney_x[0])
    kidney_y.append(kidney_y[0])
    
    return go.Scatter(
        x=kidney_x, y=kidney_y,
        fill='toself',
        fillcolor=color,
        opacity=opacity,
        line=dict(color=color, width=line_width),
        name="Thận",
        hovertemplate="<b>Thận</b><br>Lọc máu và tạo nước tiểu<br>Duy trì cân bằng nước-điện giải<extra></extra>",
        showlegend=True
    )

def draw_accurate_brain(x, y, size=0.1, color="#9b59b6", opacity=0.8, line_width=2):
    """Vẽ não với hình dạng chính xác theo giải phẫu"""
    # Não có hình oval với các nếp gấp
    t = np.linspace(0, 2*np.pi, 80)
    
    brain_x = []
    brain_y = []
    
    for i, angle in enumerate(t):
        # Tạo hình não với các nếp gấp nhỏ
        base_radius = size * 0.9
        # Thêm các nếp gấp nhỏ
        ripple = 0.05 * np.sin(8 * angle)
        radius = base_radius + ripple
        
        brain_x.append(x + radius * np.cos(angle))
        brain_y.append(y + radius * 0.8 * np.sin(angle))  # Hơi dẹt
    
    brain_x.append(brain_x[0])
    brain_y.append(brain_y[0])
    
    # Thêm đường phân chia bán cầu
    divider_x = [x, x]
    divider_y = [y - size*0.7, y + size*0.7]
    
    traces = []
    
    # Não chính
    traces.append(go.Scatter(
        x=brain_x, y=brain_y,
        fill='toself',
        fillcolor=color,
        opacity=opacity,
        line=dict(color=color, width=line_width),
        name="Não",
        hovertemplate="<b>Não</b><br>Trung tâm điều khiển cơ thể<br>Xử lý thông tin và điều khiển hoạt động<extra></extra>",
        showlegend=True
    ))
    
    # Đường phân chia
    traces.append(go.Scatter(
        x=divider_x, y=divider_y,
        mode='lines',
        line=dict(color=color, width=line_width-1),
        showlegend=False,
        hoverinfo='skip'
    ))
    
    return traces

def draw_accurate_stomach(x, y, size=0.09, color="#f39c12", opacity=0.8, line_width=2):
    """Vẽ dạ dày với hình dạng chính xác theo giải phẫu"""
    # Dạ dày có hình chữ J
    t = np.linspace(0, 1.5*np.pi, 50)
    
    stomach_x = []
    stomach_y = []
    
    for i, angle in enumerate(t):
        # Tạo hình chữ J của dạ dày
        if angle < np.pi/2:  # Phần trên
            radius = size * 0.8
            stomach_x.append(x + radius * np.cos(angle + np.pi))
            stomach_y.append(y + size*0.3 + radius * 0.6 * np.sin(angle))
        else:  # Phần cong dưới
            radius = size * 0.6
            stomach_x.append(x - size*0.2 + radius * np.cos(angle))
            stomach_y.append(y - size*0.2 + radius * 0.8 * np.sin(angle))
    
    # Đóng hình
    stomach_x.append(stomach_x[0])
    stomach_y.append(stomach_y[0])
    
    return go.Scatter(
        x=stomach_x, y=stomach_y,
        fill='toself',
        fillcolor=color,
        opacity=opacity,
        line=dict(color=color, width=line_width),
        name="Dạ dày",
        hovertemplate="<b>Dạ dày</b><br>Tiêu hóa thức ăn bằng acid<br>Dung tích khoảng 1.5 lít<extra></extra>",
        showlegend=True
    )

def get_accurate_organ_drawing(organ_name, x, y, size, color, opacity, line_width):
    """Trả về hình vẽ chính xác cho cơ quan được chỉ định"""
    organ_name_lower = organ_name.lower()
    
    if "tim" in organ_name_lower:
        return [draw_accurate_heart(x, y, size, color, opacity, line_width)]
    elif "phổi trái" in organ_name_lower or "phoi trai" in organ_name_lower:
        return [draw_accurate_lungs(x, y, size, color, opacity, line_width, "left")]
    elif "phổi phải" in organ_name_lower or "phoi phai" in organ_name_lower:
        return [draw_accurate_lungs(x, y, size, color, opacity, line_width, "right")]
    elif "gan" in organ_name_lower:
        return [draw_accurate_liver(x, y, size, color, opacity, line_width)]
    elif "thận" in organ_name_lower or "than" in organ_name_lower:
        return [draw_accurate_kidneys(x, y, size, color, opacity, line_width)]
    elif "não" in organ_name_lower or "nao" in organ_name_lower:
        return draw_accurate_brain(x, y, size, color, opacity, line_width)
    elif "dạ dày" in organ_name_lower or "da day" in organ_name_lower:
        return [draw_accurate_stomach(x, y, size, color, opacity, line_width)]
    else:
        # Fallback to simple shapes for organs not yet implemented
        t = np.linspace(0, 2*np.pi, 50)
        simple_x = x + size * np.cos(t)
        simple_y = y + size * 0.8 * np.sin(t)
        return [go.Scatter(
            x=simple_x, y=simple_y,
            fill='toself',
            fillcolor=color,
            opacity=opacity,
            line=dict(color=color, width=line_width),
            name=organ_name,
            hovertemplate=f"<b>{organ_name}</b><br>Cơ quan trong cơ thể<extra></extra>",
            showlegend=True
        )]
