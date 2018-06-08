export default class extends React.Component {
state = {
    username: '',
    message: '',
}
handleChangeName = (event) => {
    this.setState({username: event.target.value})
}

handleChangeMessage = (event) => {
    this.setState({message: event.target.value})
}

handleSubmit = (event) => {
    event.preventDefault()
    const chatMessage = new FormData()
    chatMessage.append('username', this.state.username)
    chatMessage.append('message', this.state.message)
    fetch("http://127.0.0.1:5000/chat", {method : "POST", body: chatMessage})
    this.setState({message: ""})
}
    render() {
        return (
            <>
              <form onSubmit={this.handleSubmit}>
          <input type="text" value={this.state.username} onChange={this.handleChangeName} required />
          <input type="text" value={this.state.message} onChange={this.handleChangeMessage} required />
          <button>Send</button>
                </form>   
                
                   
                
            </>
        )
    } 
}