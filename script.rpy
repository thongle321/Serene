# Define the main character
define mc = Character("Levis", color="#FFA500")

# Define the locations
image night street = im.Scale('bg/night_street.jpg',1920 ,1080)
# Start the story
label start:
    scene night street
    with fade
    pause(1.5)
    mc "Tôi đi bộ trong đêm cảm thấy một cảm giác kỳ lạ khi chân bước của tôi bước trên những đường phố còn vắng lặng."
    mc "Những đèn đường lung linh rực rỡ như những ngôi sao nhỏ lấp lánh trên bầu trời đêm."
    mc "Tôi cảm thấy mình như một thương nhân của đêm, với một mình giữa những con đường còn vắng lặng của thành phố này."
    mc "Bỗng nhiên tôi dừng lại để ngắm nhìn đôi mắt người phụ nữ đang nhìn chằm chằm vào tôi,"
    mc "quán cà phê nhỏ với những cửa sổ to, ánh sáng vàng ấm áp tỏa ra từ bên trong và những cuộc nói chuyện của những người lạ tán gẫu vui vẻ."
    mc "Trái tim tôi rạo rực khi suy nghĩ về những cuộc phiêu lưu trong những nơi xa lạ, những bất ngờ thú vị và rất nhiều câu chuyện."
    mc "Tôi tiếp tục đi bộ, đến nơi đến chốn, tìm được căn hộ mới của mình tại. Căn hộ nhỏ bé, nhưng đầy đủ tiện nghi."
    mc "Tôi cảm thấy hạnh phúc khi biết rằng đây sẽ là nơi tôi bắt đầu hành trình của mình, một cuộc hành trình vô tận, đầy màu sắc và những kỉ niệm khó quên."
    mc "Tối hôm đó, tôi ngồi trên giường nhìn ra khung cửa sổ và nhìn thấy ánh đèn đường vẫn còn sáng. "
    mc "Tôi cảm thấy mình là một phần của thế giới này. Một phần của cuộc sống này."
    mc "Tôi nhận ra rằng, dù cho cuộc sống có khó khăn đến đâu, tôi vẫn có thể vượt qua nó nếu tôi không từ bỏ và tiếp tục đi đến phía trước."
    mc "Tôi quyết tâm rằng tôi sẽ không để bản thân mình bị lạc lối giữa đám đông và sẽ luôn đi tìm kiếm hướng đi đúng đắn cho cuộc đời của mình."
    mc "Cuối cùng, tôi nhắm mắt lại và từ từ đưa mình vào giấc ngủ, mang trong mình niềm hy vọng và niềm tin vào tương lai."
    mc "Bởi vì tôi biết rằng hành trình sẽ không dễ dàng, nhưng tôi cảm thấy rằng tôi đã sẵn sàng để đối mặt với mọi thử thách và vượt qua chúng."
    mc "Tôi sẽ không từ bỏ ước mơ của mình, và sẽ luôn đặt trái tim và tâm hồn của mình vào những điều tuyệt vời nhất mà cuộc đời có thể mang đến."
    # End the story
    return