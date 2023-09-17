```
	function zoom() {
		enlarged = !enlarged;
		currentClass = enlarged ? 'enlarged' : 'reduced';

		let originalTransform = card.style.transform;

		// Temporarily remove all transformations to measure the initial center
		card.style.transform = '';

		let viewportCenter = window.innerWidth / 2;
		let cardRect = card.getBoundingClientRect();
		let cardCenter = cardRect.left + cardRect.width / 2;

		// Restore original transformations
		card.style.transform = originalTransform;

		let distanceX = viewportCenter - cardCenter;

		if (enlarged) {
			card.style.transform = `translateX(${distanceX}px)`;
		} else {
			card.style.transform = ''; // Reset the transform
		}
	}
</script>
```