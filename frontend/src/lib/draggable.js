export function draggable(node) {
  let x, y, dx = 0, dy = 0;

  function handleMousedown(event) {
    x = event.clientX - dx;
    y = event.clientY - dy;

    node.style.willChange = 'transform';

    window.addEventListener('mousemove', handleMousemove);
    window.addEventListener('mouseup', handleMouseup);
  }

  function handleMousemove(event) {
    dx = event.clientX - x;
    dy = event.clientY - y;

    node.style.transform = `translate(${dx}px, ${dy}px)`;
  }

  function handleMouseup() {
    node.style.willChange = 'auto';

    window.removeEventListener('mousemove', handleMousemove);
    window.removeEventListener('mouseup', handleMouseup);
  }

  node.addEventListener('mousedown', handleMousedown);

  return {
    destroy() {
      node.removeEventListener('mousedown', handleMousedown);
      window.removeEventListener('mousemove', handleMousemove);
      window.removeEventListener('mouseup', handleMouseup);
    },
  };
}

