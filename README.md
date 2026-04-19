# SDN-Based Firewall using POX and Mininet

## 📌 Problem Statement

This project implements a Software Defined Networking (SDN) based firewall using the POX controller and Mininet emulator. The firewall applies match–action rules to control network traffic based on IP address, MAC address, and TCP port.

---

## 🎯 Objectives

* Understand SDN architecture (control plane vs data plane)
* Implement flow rule-based filtering using OpenFlow
* Demonstrate selective traffic blocking
* Analyze network behavior under different scenarios

---

## 🧠 Concept

In SDN, the control logic is separated from the network devices. The controller (POX) installs flow rules in the switch. These rules follow a match–action model:

* Match specific packet fields (IP, MAC, port)
* Apply actions (allow or drop)

---

## 🛠️ Tools & Technologies

* Mininet (network emulator)
* POX Controller
* OpenFlow Protocol
* Python

---

## 🌐 Network Topology

Single switch topology with 3 hosts:

h1 ---
s1
h2 ---/

h3

---

## ⚙️ Implementation Details

### Firewall Rules:

1. Block traffic from IP `10.0.0.1`
2. Block traffic from MAC `00:00:00:00:00:01`
3. Block TCP traffic on port `80` (HTTP)
4. Allow all other traffic (default rule)

---

## ▶️ Execution Steps

### Step 1: Start POX Controller

```bash
cd ~/pox
./pox.py firewall
```

### Step 2: Start Mininet

```bash
sudo mn --topo single,3 --controller=remote
```

### Step 3: Test Connectivity

```bash
pingall
```

---

## 🧪 Test Scenarios

### ✅ Scenario 1: Normal Network (without firewall)

* Using `forwarding.l2_learning`
* Result: 0% packet loss

### ❌ Scenario 2: Firewall Active

* Traffic from h1 is blocked
* Partial communication failure observed

---

## 📊 Results

| Scenario | Result           |
| -------- | ---------------- |
| Normal   | 0% packet loss   |
| Firewall | ~66% packet loss |

---

## 📸 Proof of Execution

* Mininet topology screenshot
* Ping results (allowed and blocked scenarios)
* Controller logs showing rule enforcement
* Flow table (optional)

---

## 🧠 Key Concepts Used

* SDN Architecture
* OpenFlow Flow Tables
* Match–Action Rules
* Packet Filtering

---

## 🎓 Conclusion

The project successfully demonstrates how SDN enables centralized and flexible control of network traffic. The firewall selectively blocks traffic based on defined rules while allowing other communication.

---

## 📚 References

* Mininet Documentation
* POX Controller Documentation
* OpenFlow Specification
