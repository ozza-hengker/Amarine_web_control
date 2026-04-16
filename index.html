<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GUI Amarine - Advanced Dashboard</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <!-- Tambahkan Socket.IO Client -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.7.2/socket.io.js"></script>
    <style>
        ::-webkit-scrollbar { width: 6px; height: 6px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb { background: #334155; border-radius: 3px; }
        ::-webkit-scrollbar-thumb:hover { background: #475569; }
        
        /* Terminal text style */
        .terminal-text {
            font-family: 'Courier New', Courier, monospace;
            font-size: 0.8rem;
            line-height: 1.4;
            white-space: pre-wrap; 
        }
    </style>
</head>
<body class="bg-slate-950 h-screen w-screen p-6 flex items-center justify-center font-sans text-slate-300 overflow-hidden">

    <!-- MAIN APPLICATION CONTAINER -->
    <div class="w-full h-full max-w-[1400px] bg-slate-900 border-2 border-slate-700 rounded-2xl shadow-2xl p-6 flex flex-col gap-6">
        
        <!-- TOP BAR: Connection & Arming -->
        <div class="flex gap-4 shrink-0">
            <button id="btn-ssh" onclick="toggleSsh()" class="px-6 py-3 bg-slate-800 border-2 border-slate-600 rounded-xl font-bold text-slate-300 hover:bg-slate-700 hover:text-white transition-all flex items-center gap-2 shadow-lg w-48 justify-center">
                <i data-lucide="wifi-off" class="w-5 h-5"></i> <span id="ssh-text">Connect Jetson</span>
            </button>
            <button id="btn-arm" onclick="toggleArm()" class="px-6 py-3 bg-slate-800 border-2 border-slate-600 rounded-xl font-bold text-slate-300 hover:bg-slate-700 hover:text-white transition-all flex items-center gap-2 shadow-lg w-48 justify-center">
                <i data-lucide="shield" class="w-5 h-5"></i> <span id="arm-text">Arm/Disarm</span>
            </button>
        </div>

        <!-- MAIN CONTENT: Split Layout -->
        <div class="flex-1 flex flex-col md:flex-row gap-6 min-h-0">
            
            <!-- LEFT COLUMN: Controls & Monitoring -->
            <div class="w-full md:w-3/5 flex flex-col gap-6 h-full">
                
                <!-- ROV MODE PANEL -->
                <div class="flex-1 bg-slate-800/40 border-2 border-slate-600 rounded-2xl relative flex items-center justify-center group hover:border-blue-500 transition-colors shadow-inner min-h-[120px]">
                    <button id="btn-rov" onclick="toggleProcess('rov')" class="absolute top-4 right-4 px-4 py-2 bg-slate-700 border border-slate-500 rounded-lg text-xs font-bold tracking-wider hover:bg-slate-600 transition-colors uppercase z-10">
                        START / STOP
                    </button>
                    <h2 class="text-3xl font-bold tracking-widest text-slate-300 group-hover:text-white transition-colors">ROV MODE</h2>
                </div>

                <!-- AUV MODE PANEL -->
                <div class="flex-1 bg-slate-800/40 border-2 border-slate-600 rounded-2xl relative flex flex-col items-center justify-center group hover:border-purple-500 transition-colors shadow-inner min-h-[120px]">
                    <button id="btn-auv" onclick="toggleProcess('auv')" class="absolute top-4 right-4 px-4 py-2 bg-slate-700 border border-slate-500 rounded-lg text-xs font-bold tracking-wider hover:bg-slate-600 transition-colors uppercase z-10">
                        START / STOP
                    </button>
                    <h2 class="text-3xl font-bold tracking-widest text-slate-300 group-hover:text-white transition-colors">AUV</h2>
                    <span class="text-lg font-mono text-slate-500 group-hover:text-purple-400 transition-colors mt-2">(boat_mover_node)</span>
                </div>

                <!-- MONITORING PANEL -->
                <div class="flex-1 bg-slate-800/40 border-2 border-slate-600 rounded-2xl p-6 flex flex-col justify-center shadow-inner min-h-[180px]">
                    <div class="font-bold text-lg text-slate-200 mb-4 border-b border-slate-600 pb-2 flex items-center gap-2">
                        <i data-lucide="activity" class="w-5 h-5 text-emerald-400"></i> Monitoring :
                    </div>
                    
                    <div class="flex flex-col gap-3 px-4 font-mono text-sm text-slate-300">
                        <div class="flex items-center">
                            <span class="w-24">- CPU</span> 
                            <span id="val-cpu" class="text-emerald-400 font-bold w-16 text-right">0%</span>
                            <div class="ml-4 flex-1 bg-slate-900 rounded-full h-1.5 overflow-hidden"><div id="bar-cpu" class="bg-emerald-500 h-full w-0 transition-all duration-500"></div></div>
                        </div>
                        <div class="flex items-center">
                            <span class="w-24">- GPU</span> 
                            <span id="val-gpu" class="text-emerald-400 font-bold w-16 text-right">0%</span>
                            <div class="ml-4 flex-1 bg-slate-900 rounded-full h-1.5 overflow-hidden"><div id="bar-gpu" class="bg-emerald-500 h-full w-0 transition-all duration-500"></div></div>
                        </div>
                        <div class="flex items-center">
                            <span class="w-24">- Memory</span> 
                            <span id="val-mem" class="text-yellow-400 font-bold w-16 text-right">0 GB</span>
                            <div class="ml-4 flex-1 bg-slate-900 rounded-full h-1.5 overflow-hidden"><div id="bar-mem" class="bg-yellow-500 h-full w-0 transition-all duration-500"></div></div>
                        </div>
                        <div class="flex items-center">
                            <span class="w-24">- Temp</span> 
                            <span id="val-temp" class="text-orange-400 font-bold w-16 text-right">0°C</span>
                            <div class="ml-4 flex-1 bg-slate-900 rounded-full h-1.5 overflow-hidden"><div id="bar-temp" class="bg-orange-500 h-full w-0 transition-all duration-500"></div></div>
                        </div>
                        <div class="flex items-center">
                            <span class="w-24">- Watt</span> 
                            <span id="val-watt" class="text-blue-400 font-bold w-16 text-right">0 W</span>
                            <div class="ml-4 flex-1 bg-slate-900 rounded-full h-1.5 overflow-hidden"><div id="bar-watt" class="bg-blue-500 h-full w-0 transition-all duration-500"></div></div>
                        </div>
                    </div>
                </div>

            </div>

            <!-- RIGHT COLUMN: Console Preview -->
            <div class="w-full md:w-2/5 h-full bg-[#0a0a0a] border-2 border-slate-700 rounded-2xl flex flex-col relative overflow-hidden shadow-2xl">
                
                <div class="absolute top-0 left-0 w-full h-10 bg-slate-800/80 backdrop-blur-sm border-b border-slate-700 flex items-center justify-between px-4 z-10">
                    <span class="font-mono text-xs font-bold tracking-widest text-slate-400">Console Preview</span>
                    <button onclick="clearConsole()" class="text-[10px] uppercase font-bold bg-slate-700 hover:bg-slate-600 text-white px-2 py-1 rounded transition-colors">Clear</button>
                </div>

                <div id="main-console" class="terminal-text p-6 pt-14 flex-1 overflow-y-auto text-slate-300">
                    <div class="text-slate-500 italic">Welcome to Amarine GCS. Waiting for connection...</div>
                </div>
            </div>

        </div>
    </div>

    <!-- JAVASCRIPT LOGIC -->
    <script>
        lucide.createIcons();

        // 1. Inisialisasi koneksi Web Socket ke app.py Backend
        const socket = io();

        // State Variables
        let sshConnected = false;
        let isArmed = false;
        const processes = {
            rov: { running: false, interval: null },
            auv: { running: false, interval: null, timer: 0 }
        };

        // Kodingan AUV Skenario (Sesuai dengan boat_mover_node.cpp milik Ozza)
        const auvScenario = [
            { t: 0.0, msg: "SIAP! Skenario 10 Detik. Yaw & Lateral sudah dibalik (Inverted)." },
            { t: 0.5, msg: "Time 0.0: STANDBY..." },
            { t: 3.0, msg: "Time 3.0: MAJU..." },
            { t: 13.0, msg: "Time 13.0: YAW KANAN (Putar)..." },
            { t: 23.0, msg: "Time 23.0: YAW KIRI (Putar)..." },
            { t: 33.0, msg: "Time 33.0: MUNCUL (Naik)..." },
            { t: 43.0, msg: "Time 43.0: MENYELAM (Turun)..." },
            { t: 53.0, msg: "Time 53.0: LATERAL KANAN (Geser)..." },
            { t: 63.0, msg: "Time 63.0: LATERAL KIRI (Geser)..." },
            { t: 73.0, msg: "Time 73.0: MUNDUR..." },
            { t: 83.0, msg: "Time 83.0: SELESAI. Stop." },
        ];

        function getTimestamp() {
            const now = new Date();
            return `[${now.getHours().toString().padStart(2, '0')}:${now.getMinutes().toString().padStart(2, '0')}:${now.getSeconds().toString().padStart(2, '0')}]`;
        }

        function appendToConsole(text, type = 'normal') {
            const con = document.getElementById('main-console');
            const div = document.createElement('div');
            
            if(type === 'error') div.className = 'text-red-400 font-bold';
            else if(type === 'success') div.className = 'text-emerald-400 font-bold';
            else if(type === 'cmd') div.className = 'text-blue-300 font-bold';
            else if(type === 'auv') div.className = 'text-purple-300';
            else div.className = 'text-slate-300';
            
            div.innerText = `${getTimestamp()} ${text}`;
            con.appendChild(div);
            con.scrollTop = con.scrollHeight; // Auto-scroll
        }

        function clearConsole() {
            document.getElementById('main-console').innerHTML = '';
        }

        // Menerima Data dari Backend
        socket.on('terminal_output', function(data) {
            appendToConsole(data.text, data.is_error ? 'error' : 'normal');
        });

        // --- BUTTON HANDLERS ---

        function toggleSsh() {
            const btn = document.getElementById('btn-ssh');
            const text = document.getElementById('ssh-text');
            const icon = btn.querySelector('i');

            if (sshConnected) {
                sshConnected = false;
                if(isArmed) toggleArm();
                if(processes.rov.running) toggleProcess('rov');
                if(processes.auv.running) toggleProcess('auv');

                btn.className = "px-6 py-3 bg-slate-800 border-2 border-slate-600 rounded-xl font-bold text-slate-300 hover:bg-slate-700 hover:text-white transition-all flex items-center gap-2 shadow-lg w-48 justify-center";
                text.innerText = "Connect Jetson";
                icon.setAttribute("data-lucide", "wifi-off");
                appendToConsole("SSH Connection Closed.", "error");
            } else {
                appendToConsole("Attempting SSH connection to amarine@ubuntu.local...", "normal");
                btn.className = "px-6 py-3 bg-slate-800 border-2 border-slate-600 rounded-xl font-bold text-slate-300 flex items-center gap-2 shadow-lg w-48 justify-center opacity-70 cursor-wait";
                text.innerText = "Connecting...";
                
                // Simulate Connection Delay
                setTimeout(() => {
                    sshConnected = true;
                    btn.className = "px-6 py-3 bg-green-900/40 border-2 border-green-600/50 rounded-xl font-bold text-green-400 hover:bg-red-900/40 hover:text-red-400 hover:border-red-600/50 transition-all flex items-center gap-2 shadow-[0_0_15px_rgba(34,197,94,0.2)] w-48 justify-center";
                    text.innerText = "Connected";
                    icon.setAttribute("data-lucide", "wifi");
                    lucide.createIcons();
                    appendToConsole("SSH Connection Established successfully!", "success");
                }, 1500);
            }
            lucide.createIcons();
        }

        function toggleArm() {
            if (!sshConnected) {
                appendToConsole("Cannot Arm: Jetson is not connected!", "error");
                return;
            }

            const btn = document.getElementById('btn-arm');
            const text = document.getElementById('arm-text');
            const icon = btn.querySelector('i');

            if (isArmed) {
                isArmed = false;
                btn.className = "px-6 py-3 bg-slate-800 border-2 border-slate-600 rounded-xl font-bold text-slate-300 hover:bg-slate-700 hover:text-white transition-all flex items-center gap-2 shadow-lg w-48 justify-center";
                text.innerText = "Arm/Disarm";
                icon.setAttribute("data-lucide", "shield");
                appendToConsole('Executing: ros2 service call /mavros/cmd/arming "{value: False}"', 'cmd');
                setTimeout(() => appendToConsole('DISARMED. Thrusters disabled.', 'error'), 500);
            } else {
                isArmed = true;
                btn.className = "px-6 py-3 bg-red-600/20 border-2 border-red-600 rounded-xl font-bold text-red-500 hover:bg-slate-800 hover:border-slate-600 hover:text-slate-300 transition-all flex items-center gap-2 shadow-[0_0_15px_rgba(220,38,38,0.3)] animate-pulse w-48 justify-center";
                text.innerText = "DISARM (KILL)";
                icon.setAttribute("data-lucide", "shield-alert");
                appendToConsole('Executing: ros2 service call /mavros/cmd/arming "{value: True}"', 'cmd');
                setTimeout(() => appendToConsole('ARMED! Thrusters are LIVE.', 'success'), 500);
            }
            lucide.createIcons();
        }

        function toggleProcess(id) {
            if (!sshConnected) {
                appendToConsole(`Cannot start ${id.toUpperCase()}: Jetson is not connected!`, "error");
                return;
            }
            if (!isArmed && id === 'auv') {
                appendToConsole(`Cannot start AUV Mission: Drone must be ARMED first!`, "error");
                return;
            }

            const btn = document.getElementById(`btn-${id}`);
            const proc = processes[id];

            // Cegah nyalakan ROV dan AUV bersamaan
            const otherId = id === 'rov' ? 'auv' : 'rov';
            if (!proc.running && processes[otherId].running) {
                appendToConsole(`Please stop ${otherId.toUpperCase()} mode before starting ${id.toUpperCase()}.`, "error");
                return;
            }

            if (proc.running) {
                // STOP PROCESS
                proc.running = false;
                clearInterval(proc.interval);
                btn.className = "absolute top-4 right-4 px-4 py-2 bg-slate-700 border border-slate-500 rounded-lg text-xs font-bold tracking-wider hover:bg-slate-600 transition-colors uppercase z-10 text-slate-300";
                
                if(id === 'auv') appendToConsole('Mission Aborted (Ctrl+C sent).', 'error');
                else appendToConsole(`${id.toUpperCase()} Mode Deactivated.`, 'normal');
                
                // Kirim request ke backend via socket
                socket.emit('kill_process', { id: id });

            } else {
                // START PROCESS
                proc.running = true;
                proc.timer = 0;
                btn.className = "absolute top-4 right-4 px-4 py-2 bg-red-600 border border-red-500 rounded-lg text-xs font-bold tracking-wider hover:bg-red-700 transition-colors uppercase z-10 text-white shadow-[0_0_10px_rgba(220,38,38,0.5)]";
                
                appendToConsole(`Starting ${id.toUpperCase()}...`, 'cmd');

                // Simulasi Script boat_mover_node yang baru
                if (id === 'auv') {
                    appendToConsole('ros2 run simple_boat boat_mover_node', 'cmd');
                    
                    let scenarioIndex = 0;
                    proc.interval = setInterval(() => {
                        proc.timer += 0.5; // simulasi tick waktu
                        
                        // Cek apakah ada pesan sesuai waktu di scenario
                        if (scenarioIndex < auvScenario.length && proc.timer >= auvScenario[scenarioIndex].t) {
                            appendToConsole(`[boat_mover_node] ${auvScenario[scenarioIndex].msg}`, 'auv');
                            scenarioIndex++;
                        }

                        // Auto stop kalau skenario habis
                        if (proc.timer > 85.0) {
                            toggleProcess('auv');
                        }
                    }, 500);
                } else if (id === 'rov') {
                    appendToConsole('ROV Teleoperation node started. Awaiting joystick input...', 'normal');
                }

                // Kirim request ke backend via socket
                socket.emit('start_process', { id: id, target: 'default' });
            }
        }

        // Hardware Monitoring Live Simulation (Meniru Jetson)
        setInterval(() => {
            if(sshConnected && Math.random() > 0.3) {
                const cpu = Math.floor(Math.random() * 30) + 15; // 15-45%
                const gpu = Math.floor(Math.random() * 50) + (processes.auv.running ? 40 : 10); // GPU naik kalau AUV jalan
                const mem = (Math.random() * 0.5 + 4.2).toFixed(1); // ~4GB
                const temp = Math.floor(Math.random() * 10) + (processes.auv.running ? 50 : 40); // 40-60C
                const watt = (Math.random() * 5 + (isArmed ? 15 : 5)).toFixed(1); // Naik kalau Armed

                document.getElementById('val-cpu').innerText = `${cpu}%`;
                document.getElementById('bar-cpu').style.width = `${cpu}%`;
                
                document.getElementById('val-gpu').innerText = `${gpu}%`;
                document.getElementById('bar-gpu').style.width = `${gpu}%`;

                document.getElementById('val-mem').innerText = `${mem} GB`;
                document.getElementById('bar-mem').style.width = `${(mem/8)*100}%`;

                document.getElementById('val-temp').innerText = `${temp}°C`;
                document.getElementById('bar-temp').style.width = `${Math.min(temp, 100)}%`;
                
                // Ubah warna temp kalau panas
                document.getElementById('bar-temp').className = temp > 55 ? "bg-red-500 h-full w-0 transition-all duration-500" : "bg-orange-500 h-full w-0 transition-all duration-500";

                document.getElementById('val-watt').innerText = `${watt} W`;
                document.getElementById('bar-watt').style.width = `${Math.min((watt/30)*100, 100)}%`;
            } else if (!sshConnected) {
                // Reset kalau disconnect
                ['cpu', 'gpu', 'mem', 'temp', 'watt'].forEach(id => {
                    document.getElementById(`val-${id}`).innerText = id === 'mem' ? '0 GB' : id === 'temp' ? '0°C' : id === 'watt' ? '0 W' : '0%';
                    document.getElementById(`bar-${id}`).style.width = '0%';
                });
            }
        }, 1500);

    </script>
</body>
</html>
