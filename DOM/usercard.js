class UserCard extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' });

    const wrapper = document.createElement('div');
    wrapper.classList.add('card');

    const img = document.createElement('img');
    img.src = this.getAttribute('avatar') || '';
    img.alt = `${this.getAttribute('name')}'s avatar`;

    const name = document.createElement('h3');
    name.textContent = this.getAttribute('name');

    const role = document.createElement('p');
    role.textContent = this.getAttribute('role');

    // Hidden details
    const details = document.createElement('div');
    details.classList.add('details');
    details.innerHTML = `
      <p><strong>Email:</strong> ${this.getAttribute('email')}</p>
      <p><strong>Location:</strong> ${this.getAttribute('location')}</p>
    `;
    details.style.display = 'none'; // Initially hidden

    // Toggle interaction + welcome message
    wrapper.addEventListener('click', () => {
      const visible = details.style.display === 'block';
      details.style.display = visible ? 'none' : 'block';

      // Show welcome message
      const userName = this.getAttribute('name') || 'there';
      alert(`Hello ${userName}, welcome to the team!`);
    });

    const style = document.createElement('style');
    style.textContent = `
      .card {
        border: 1px solid #ccc;
        border-radius: 12px;
        padding: 10px;
        text-align: center;
        width: 180px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        margin: 10px;
        font-family: sans-serif;
        transition: transform 0.2s ease;
        cursor: pointer;
      }
      .card:hover {
        transform: scale(1.05);
      }
      img {
        border-radius: 50%;
        width: 80px;
        height: 80px;
      }
      h3 {
        margin: 8px 0 4px;
        font-size: 1.1em;
      }
      p {
        margin: 0;
        color: gray;
        font-size: 0.9em;
      }
      .details {
        margin-top: 8px;
        color: #333;
        font-size: 0.85em;
        background: #f9f9f9;
        border-radius: 8px;
        padding: 6px;
      }
    `;

    this.shadowRoot.append(style, wrapper);
    wrapper.append(img, name, role, details);
  }
}

customElements.define('user-card', UserCard);
