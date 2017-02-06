'''
{%for topic in topics%}
	<p> {{topic.name}} <a href = "{{ url_for('poems',topic_id= topic.id)}}">poems</a>  <a href = "{{url_for('quotes', topic_id = topic.id )}}">quotes</a> </p>
{%endfor%}	
''' <html>


{% for topic in topics%}

<a href='#'>{{ topic.name }} </br> </a>

{% endfor %}


 </html>}


poems.html

 <h1> poems title</h1>

{%if topic==[]%}
<p> there are currently no poems in the catalog. </p>
{%else%}
<div class ="poem">
	{%for topic in topics%}
	<a href = {{url_for('poem', poem_id = topic.id)}}>
		<p> {{topic.name}}</p>
	</a>
	{%endfor%}
</div>
{% endif %}		

<h1> quote title</h1>

{%if topic==[]%}
<p> there are currently no quotes in the catalog. </p>
{%else%}
<div class ="quote">
	{%for topic in topics%}
	<a href = {{url_for('quote', quote_id = topic.id)}}>
		<p> {{topic.name}}</p>
	</a>
	{%endfor%}
</div>
{% endif %}		


