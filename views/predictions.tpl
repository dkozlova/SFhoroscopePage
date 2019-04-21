<html>
	<head>
		<meta charset='utf-8'>
		<title>Гороскоп на сегодня</title>
		 <script src="http://code.jquery.com/jquery-3.3.1.min.js"></script>
		 
		<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
			
			
	</head>
	<body>
		<div class = "container">
			<h1 id="main_header">Что день {{date}} готовит</h1>
			
			% if special_date:
			<h2>Сегодня особенный день!</h2>
			%end
			<div class="row">
				<div class="col" id="p-0"></div>
				<div class="col" id="p-1"></div>
				<div class="col" id="p-2"></div>
			</div>	
			
			<div class="row">
				<div class="col"  id="p-3"></div>
				<div class="col"  id="p-4"></div>
				<div class="col"  id="p-5"></div>
			  </div>
			
			<hr> <a href="about.html"> О реализации </a> 
		</div>
	</body>
	
	<script language = 'javascript'>
		
		advice_url = "http://sf-pyw.mosyag.in/m04/api/forecasts"

	$("#main_header").click(function() {
	
		$.getJSON(advice_url, function(data){
			
			msg = data["prophecies"]
			set_content_in_divs(msg)
			})
	});


function set_content_in_divs(msg) {
  $.each(msg, function(i, d) {
    p = $("#p-" + i)
    p.html("<p>" + d + "</p>")
})
}
	</script>
</html>
