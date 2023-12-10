# TextDisplay

$ sudo apt-get install python3-gi gir1.2-gtk-3.0
#TODO
1. ROS Module stt_interface에서 pub하는 text를 sub하는 ROS Module로 구조 변경
2. catkin_ws에서 "catkin_create_pkg text_display std_msgs rospy" 명령어로 새 패키지 생성
3. action_execution_pkg/Config/mybom2.2.json 및 tcm.json 수정하여 text_display를 자동실행 모듈에 추가
(또는, 자동실행 모듈에 추가하지 않고 autorun 스크립트 파일에 실행 커맨드로 추가)
