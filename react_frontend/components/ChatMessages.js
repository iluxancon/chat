export default class extends React.Component {
    state = {
        chatMessages: null,
    }

    fetchChatMessages = () => {
        fetch("http://127.0.0.1:5000/chat")
            .then((data) => data.json())
            .then((chatMessages) => this.setState ({ chatMessages } ))    

    }
    componentDidMount() {
        setInterval(this.fetchChatMessages, 1000)
        }

    render() {
        if (this.state.chatMessages===null) {
            return <div>Chat is empty :(...</div>
        }
        return (
            <>
                <ul>
                    {this.state.chatMessages.map(
                        (chatMessage) => (
                            <li>
                                <span>{`${chatMessage.username}--`}</span>
                                <span>{chatMessage.message}</span>
                            </li>
                        )
                    )
                    }
                </ul>
            </>
        )
    }
}