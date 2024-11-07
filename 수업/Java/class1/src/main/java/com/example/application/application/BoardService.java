package com.example.application.application;

import com.example.application.presentation.dto.BoardFindById;
import com.example.application.presentation.dto.BoardSaveDto;
import com.example.application.data.entity.Board;
import com.example.application.data.BoardRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
@RequiredArgsConstructor
public class BoardService {
    private final BoardRepository boardRepository;

    public void save(BoardSaveDto dto) {
        Board board = new Board();
        board.setTitle(dto.getTitle());
        board.setContent(dto.getContent());

        boardRepository.save(board);
    }

    public BoardFindById findById(Long id) {
        Board board = boardRepository.findById(id).get();
        BoardFindById boardFindById = new BoardFindById();
        boardFindById.setId(board.getId());
        boardFindById.setTitle(board.getTitle());
        boardFindById.setContent(board.getContent());
        return boardFindById;
    }

    public List<BoardFindById> findAll() {
        List<Board> boards = boardRepository.findAll();

        List<BoardFindById> boardFindByIds = new ArrayList<>();
        for(Board board : boards) {
            BoardFindById boardFindById = new BoardFindById();
            boardFindById.setId(board.getId());
            boardFindById.setTitle(board.getTitle());
            boardFindById.setContent(board.getContent());
            boardFindByIds.add(boardFindById);
        }

        return boardFindByIds;
    }

    public void delete(Long id) {
        boardRepository.deleteById(id);
    }

    public void put(Long id, BoardSaveDto dto) {
        Board board = boardRepository.findById(id).get();
        board.setTitle(dto.getTitle());
        board.setContent(dto.getContent());
        boardRepository.save(board);
    }
}
