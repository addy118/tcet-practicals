function item(props) {
    return (
        <div>
            <div>
                {props.category}
            </div>
            <div>
                <img src="{props.category}.jpg" alt="{props.category}"></img>
            </div>
        </div>
    );
}