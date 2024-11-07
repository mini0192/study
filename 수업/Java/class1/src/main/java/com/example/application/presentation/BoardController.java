package com.example.application.presentation;

import com.example.application.presentation.dto.BoardFindById;
import com.example.application.presentation.dto.BoardSaveDto;
import com.example.application.application.BoardService;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Controller
@RequestMapping("/boards")
@RequiredArgsConstructor
public class BoardController {

    private final BoardService boardService;

    @GetMapping
    public String findAll(Model model) {
        List<BoardFindById> boardFindByIds = boardService.findAll();
        model.addAttribute("boards", boardFindByIds);
        return "board/list";
    }

    @GetMapping("/{id}")
    public String findById(@PathVariable("id") Long id, Model model) {
        BoardFindById boardFindById = boardService.findById(id);
        model.addAttribute("board", boardFindById);
        return "board/detail";
    }

    @GetMapping("/write")
    public String save() {
        return "board/write";
    }

    @PostMapping
    public String save(@ModelAttribute BoardSaveDto dto) {
        boardService.save(dto);
        return "redirect:/boards";
    }

    @PostMapping("/delete/{id}")
    public String delete(@PathVariable("id") Long id) {
        boardService.delete(id);
        return "redirect:/boards";
    }

    @GetMapping("/put/{id}")
    public String put(@PathVariable("id") Long id, Model model) {
        BoardFindById boardFindById = boardService.findById(id);
        model.addAttribute("board", boardFindById);
        return "board/put";
    }

    @PostMapping("/put/{id}")
    public String put(@PathVariable("id") Long id, @ModelAttribute BoardSaveDto dto) {
        boardService.put(id, dto);
        return "redirect:/boards";
    }

//    @PostMapping
//    public String save(@RequestParam("title") String title, @RequestParam("content") String content) {
//        System.out.println(title);
//        System.out.println(content);
//        return "redirect:/boards";
//    }
}
