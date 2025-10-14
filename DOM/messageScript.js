class MessageBox extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' });

    const container = document.createElement('div');
    const button = document.createElement('button');
    const message = document.createElement('p');

    button.textContent = 'Click Here for surprise message';
    message.textContent = 'Surprise, Click the button';


    const style = document.createElement('style');
    style.textContent = `
     div {
            font-family: Arial, sans-serif;
            border: 1px solid #ccc;
            border-radius: 8px;
            padding: 15px;
            width: 200px;
            text-align: center;
            box-shadow: 0 2px 4px rgba(0,0,0,0.2);
          }
          button {
            margin-top: 10px;
            padding: 8px 12px;
            background: royalblue;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
          }
          button:hover {
            background: dodgerblue;
          }
          p {
            color: #333;
          }
        `;

        button.addEventListener('click', () => {
            message.textContent ='Hello, NO Surprise !';
        });


        container.append(button, message);
        this.shadowRoot.append(style, container);
    }
}

customElements.define('message-box', MessageBox);
