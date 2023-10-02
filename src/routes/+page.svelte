<script>
  let randomNumber = 0;

  async function getRandomNumber() {
    const r = await fetch('/random');
    const d = await r.json();
    return (randomNumber = d);
  }

  $: randomNumber;
</script>

<h1>Your number is {randomNumber}!</h1>
<button on:click="{getRandomNumber}">Get a random number</button>
