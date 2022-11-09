function Conteudo() {
    return (
      <div className="Conteudo">
        <div className="conteudo--escrever">
            <textarea id="texto--escrito" name="texto-escrito"
                        rows="12" placeholder="Escreva aqui:" />
        </div>
        {/*<div className="add--seccao">
            <input type="text" placeholder="Nome da seção"/>
            <input type="text" placeholder="Título"/>
        </div>*/}
      </div>
    );
  }
  
  export default Conteudo;
  